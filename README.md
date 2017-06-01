# TOC Project 2017

* A telegram bot based on a finite state machine
* Help people to stretch their muscle

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
* The initial state is set to `user`.
Input `/start` to wake the bot, and it will list acceptable inputs. 

* The user will be asked to choose a part of his body, then choose the proper muscle. The bot will reply how to stretch the muscle.

* The knowledge of stretching is from NCKU PAIN FREE FOR LIFE COURSE
## Author
[zmke](https://github.com/zmke)
