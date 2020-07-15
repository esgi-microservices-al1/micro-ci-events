from consul import Consul, Check


class ConsulManager(object):
    def __init__(self, host, port, token):
        self.host = host
        self.port = port
        self.token = token
        self.consulClient = None
        self.isHealthy = False

    def init_client(self):
        if self.consulClient is None:
            self.consulClient = Consul(host=self.host)

    def register_service(self):
        self.consulClient.agent.service.register(name="micro-ci-events-al1", service_id="micro-ci-events-al1")

    def heathcheck(self):
        index, checks = self.consulClient.health.checks('micro-ci-events-al1')
        for check in checks:
            if check['ServiceID'] == ['micro-ci-events-al1']:
                self.isHealthy = True

    def deregister_service(self):
        if(self.isHealthy):
            self.consulClient.agent.service.deregister('events-al1')

    def register(self):
        self.init_client()
        self.heathcheck()
        if not self.isHealthy:
            self.deregister_service()
        self.register_service()