FROM ubuntu:18.04
RUN apt-get update 
RUN apt install sudo -y
RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

CMD /bin/bash



# RUN whoami
# RUN sudo apt update
# RUN sudo apt install python3 python3-pip python3-virtualenv build-essential python3-dev -y
# RUN python3 -m virtualenv --python=python3 --system-site-packages orange3venv
# RUN chmod +x orange3venv/bin/activate
# RUN python3 -m virtualenv  --python=python3 orange3venv
# RUN pip3 install --user  PyQt5 PyQtWebEngine -y
# RUN pip3 install --user orange3 -y
# CMD python3 -m Orange.canvas
