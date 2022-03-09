# exemplaris

## Python setup
1. `virtualenv -ppython3.9 venv`
2. `. venv/bin/activate`
3. `pip install -r requirements.txt`
4. You're good to go.

## MQ Broker
To start ActiveMQ broker

1. download [ActiveMQ](https://activemq.apache.org/components/classic/download/) 
2. extract 
3. cd bin/ 
4. activemq.jar start
5. open Browser at http://127.0.0.1:8161/
6. user: admin, pw: admin



With running ActiveMQ Broker, run subsubExample.py to see dataflow between the two main processes.



To create mockdata use : https://www.mockaroo.com/
