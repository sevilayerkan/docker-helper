import subprocess
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


class DockerHelper:
    def show(self):
        output = subprocess.check_output('docker ps -a', shell=True).decode()
        return output

    def start(self, container_name):
        try:
            subprocess.check_output(
                f'docker start {container_name}', shell=True)
            return f"Container '{container_name}' started successfully."
        except subprocess.CalledProcessError:
            return f"Error: Failed to start container '{container_name}'."

    def stop(self, container_name):
        try:
            subprocess.check_output(
                f'docker stop {container_name}', shell=True)
            return f"Container '{container_name}' stopped successfully."
        except subprocess.CalledProcessError:
            return f"Error: Failed to stop container '{container_name}'."

    def restart(self, container_name):
        try:
            subprocess.check_output(
                f'docker restart {container_name}', shell=True)
            return f"Container '{container_name}' restarted successfully."
        except subprocess.CalledProcessError:
            return f"Error: Failed to restart container '{container_name}'."

    def deleteContainer(self, container_name):
        try:
            subprocess.check_output(f'docker rm {container_name}', shell=True)
            return f"Container '{container_name}' deleted successfully."
        except subprocess.CalledProcessError:
            return f"Error: Failed to delete container '{container_name}'."

    def deleteImage(self, image_name):
        try:
            subprocess.check_output(f'docker rmi {image_name}', shell=True)
            return f"Image '{image_name}' deleted successfully."
        except subprocess.CalledProcessError:
            return f"Error: Failed to delete image '{image_name}'."

    def mount(self, container_name, host_path, container_path):
        try:
            subprocess.check_output(
                f'docker run -v {host_path}:{container_path} --name {container_name} -d image_name', shell=True)
            return "Volume mounted successfully."
        except subprocess.CalledProcessError:
            return "Error: Failed to mount volume."


# Create an instance of DockerHelper
docker = DockerHelper()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/containers', methods=['GET'])
def get_containers():
    containers = docker.show()
    return jsonify({'message': containers})


@app.route('/operation', methods=['POST'])
def perform_operation():
    operation = request.form['operation']
    container_name = request.form['container_name']
    host_path = request.form['host_path']
    container_path = request.form['container_path']
    result = ""

    if operation == "start":
        result = docker.start(container_name)
    elif operation == "stop":
        result = docker.stop(container_name)
    elif operation == "restart":
        result = docker.restart(container_name)
    elif operation == "deleteContainer":
        result = docker.deleteContainer(container_name)
    elif operation == "deleteImage":
        result = docker.deleteImage(container_name)
    elif operation == "mount":
        result = docker.mount(container_name, host_path, container_path)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
