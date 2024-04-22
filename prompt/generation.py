def generate(product: str, template: str) -> str:
	args = [product]
	formatted_prompt = template.format(args)
	return formatted_prompt