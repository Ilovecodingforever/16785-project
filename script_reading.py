from pylips.speech import RobotFace
from pylips.face import FacePresets




def read_from_ssh():
    import paramiko

    # SSH connection details
    hostname = "lop2.autonlab.org"
    username = "mingzhul"
    password = "<P$$Cu;{2xD$#l,qh(:3k+8`:"  # Consider using SSH keys for better security
    remote_file_path = "16785-project/script.txt"
    local_file_path = "script.txt"

    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (less secure, for testing purposes only)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh_client.connect(hostname=hostname, username=username, password=password)

        # Open an SFTP session
        sftp_client = ssh_client.open_sftp()

        # Download a file from the remote server
        sftp_client.get(remote_file_path, local_file_path)
        print(f"File downloaded successfully to {local_file_path}")

        # Upload a file to the remote server
        # sftp_client.put(local_file_path, remote_file_path)
        # print(f"File uploaded successfully to {remote_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the SFTP and SSH connections
        if sftp_client:
            sftp_client.close()
        if ssh_client:
            ssh_client.close()    




read_from_ssh()


# read the script
with open("script.txt", "r") as file:
    reply = file.read()


face = RobotFace()
face.say(reply)

