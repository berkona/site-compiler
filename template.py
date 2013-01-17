class Template(object):

	BODY_MAGIC_WORD = '__SITE_COMPILER_BODY__'

	def __init__(self, path):
		with open(path, mode='r', encoding='utf-8') as templateFile:
			self.rawTemplate = templateFile.read()

		self.bodyIdx = self.rawTemplate.index(Template.BODY_MAGIC_WORD)

	def format(self, body):
		start = self.bodyIdx
		end = self.bodyIdx + len(Template.BODY_MAGIC_WORD)
		return self.rawTemplate[:start] + body + self.rawTemplate[end:]
