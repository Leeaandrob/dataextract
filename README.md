Desafio Simbiose Ventures
==========================

Sistema de consulta de restaurantes do RJ

--------------------------

Serviço de Fila
$ sudo apt-get install rabbitmq-server
$ sudo rabbitmqctl add_user simbiosevetures simbiose741258
$ sudo rabbitmqctl add_vhost simbiosevetureshost
$ sudo rabbitmqctl set_permissions -p simbiosevetureshost simbiosevetures ".*" ".*" ".*"
