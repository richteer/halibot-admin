from halibot import HalModule

class Admin(HalModule):

	def init(self):
		self.commands = {
			"!reload": self._reload
		}

	def receive(self, msg):
		ls = msg.body.split(' ')
		if not len(ls):
			return
		cmd = ls[0]
		arg = ' '.join(ls[1:]).strip()

		self.commands.get(cmd,lambda y,z: None)(msg, arg)

	def _reload(self, msg, arg):
		self._hal.reload(arg)
		self.reply(msg, body="Attempted to reload '{}'".format(arg))
