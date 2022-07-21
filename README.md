# Image Super Resolution using SRGAN model
- The project: SRGANupscaling
- Description: Web-app to upscale images by 4x built as a python package implementing CI-CD
- Data Source: DIV2K imageset
- Model used: SRGAN model with ResNet blocks as generator and a VGG19 based discriminator employing a perceptual loss function
- References: https://arxiv.org/pdf/1609.04802.pdf

# Testing done on SET5 dataset
![Alt text](srgan_results/baby.png?raw=true)
![Alt text](srgan_results/bird.png?raw=true)
![Alt text](srgan_results/butterfly.png?raw=true)
![Alt text](srgan_results/head.png?raw=true)
![Alt text](srgan_results/woman.png?raw=true)

# Try out the web-app

https://srgan-upscale-2xv4a765yq-ey.a.run.app

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

# Install

Go to `https://github.com/sridhar211/SRGANupscaling` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:sridhar211/SRGANupscaling.git
cd SRGANupscaling
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
SRGANupscaling-run
```
