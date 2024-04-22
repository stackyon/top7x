import unittest

from prompt import generation


class TestPromptGeneration(unittest.TestCase):
	
	def test_generate(self):
		product = 'gameboy'
		template = 'The product is a {product}'
		prompt = generation.generate(product, template)
		assert prompt == 'The product is a gameboy'