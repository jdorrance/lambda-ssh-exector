import paramiko

def my_handler(event, context):
    client = None
    print("beginning ssh command")
    output = ""
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(event['hostname'], port=22, username=event['username'], password=event['password'])

        stdin, stdout, stderr = client.exec_command(event['command'], get_pty=True)

        for line in stdout.readlines():
            output = output + line
        for line in stderr.readlines():
            output = output + line
        if output != "":
            print(output)
        else:
            print("There was no output for this command")
    finally:
        if client:
            print("closing ssh client")
            client.close()
    return output



my_handler(event, "")
