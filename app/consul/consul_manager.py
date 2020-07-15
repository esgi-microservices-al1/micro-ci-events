from consul import Consul, Check


class ConsulManager(object):
    def __init__(self, host):
        self.host = host
        # self.port = port
        # self.token = token
        self.consulClient = None
        self.isHealthy = False

    def init_client(self):
        if self.consulClient is None:
            self.consulClient = Consul(host=self.host)

    def register_service(self):
        self.consulClient.agent.service.register(name="events_al1", service_id="events_al1", check=Check.ttl('10s'))

    def heathcheck(self):
        index, checks = self.consulClient.health.checks('events_al1')
        for check in checks:
            if check['ServiceID'] == ['evenst_al1']:
                self.isHealthy = True

    def deregister_service(self):
        if(self.isHealthy):
            self.consulClient.agent.service.deregister('events_al1')

    def register(self):
        self.init_client()
        self.heathcheck()
        self.register_service()