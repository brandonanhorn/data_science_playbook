First provision the machine:

```
ssh root@<ip address>
yes
adduser brandon
# <password>
y
usermod -aG sudo brandon
ufw app list
ufw allow OpenSSH
ufw enable
y
rsync --archive --chown=brandon:brandon ~/.ssh /home/brandon
```

First download

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Then install

```
bash Miniconda3-latest-Linux-x86_64.sh
```

Then click through all the junk

Then restart connection by running:

```
ssh brandon@<ip address>
```

Now update everything:

```
ssh brandon@<ip address>
sudo apt update
# <password>
sudo apt -y upgrade
```

Now install Jupyter:

```
sudo apt install python-pip
pip install jupyter
```

Now in a fresh terminal that is running on your machine run the following command:

```
ssh -L 8888:localhost:8888 brandon@<ip address>
```

```
sudo apt install jupyter-core
jupyter notebook
```

Paste something that looks like this into your regular browser window:

```
http://127.0.0.1:8888/?token=9202fb23462021c9b6becc5f72ba1c912c6dffdeb9b1e2e8
```





