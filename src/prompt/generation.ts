const fs = require('fs');


function generate(product: string, template: string = 'basic'): string {
	let template_text: string = fs.readFile('${template}.txt', 'utf8');
	let args: Array<string> = [product]
	let formatted_prompt = format(template_text, args);
	return formatted_prompt
}


function format(template: string, args: string[]): string {
	return template.replace(/{(\d+)}/g, function(match, number) { 
		return typeof args[number] != 'undefined'
		? args[number]
		: match;
	});
}