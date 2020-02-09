"""Module for converting a markdown file"""

import os
import re

def findFiles(directory):
	files = os.listdir(directory)
	#create list of all markdown files in directory
	markdowns = [(directory + '\\' + file) for file in files if file.endswith('.mmd')]
	for markdownfile in markdowns:
		formatFileBBcode(markdownfile)

def parseStringBBcode(line):
	formattingFunctions = [strongMarkdowntoBBcode, boldMarkdowntoBBcode, italicMarkdowntoBBcode]
	for formatFunc in formattingFunctions:
		line = formatFunc(line)
	return line
	
def boldMarkdowntoBBcode(line):
	"""Takes a string and returns a single BBcode string with bold formatting"""
	#explode into bold parts
	boldParts = re.split(r'(\*{2,2}.+?\*{2,2})', line)
	for part in range(len(boldParts)):
		if boldParts[part - 1].startswith('**'): boldParts[part - 1] = '[B]' + boldParts[part - 1].lstrip('**')
		if boldParts[part - 1].endswith('**'): boldParts[part - 1] = boldParts[part - 1].rstrip('**') + '[/B]'
	return ''.join(boldParts)

def strongMarkdowntoBBcode(line):
	strongParts = re.split(r'(\*{3,3}.+?\*{3,3})', line)
	for part in range(len(strongParts)):
		if strongParts[part - 1].startswith('***'): strongParts[part - 1] = '[B][I]' + strongParts[part - 1].lstrip('***')
		if strongParts[part - 1].endswith('***'): strongParts[part - 1] = strongParts[part - 1].rstrip('***') + '[/I][/B]'
	return ''.join(strongParts)

def italicMarkdowntoBBcode(line):
	italicParts = re.split(r'(\*{1,1}.+?\*{1,1})', line)
	for part in range(len(italicParts)):
		if italicParts[part - 1].startswith('*'): italicParts[part - 1] = '[I]' + italicParts[part - 1].lstrip('*')
		if italicParts[part - 1].endswith('*'): italicParts[part - 1] = italicParts[part - 1].rstrip('*') + '[/I]'
	return ''.join(italicParts) 

def formatFileBBcode(file):
	with open(file,'r', encoding='utf-8') as markdown:
		lines = markdown.readlines()
		formatted = []
		for line in lines:
			line = line.replace('\n','\n\n') #add double lines for each paragraph
			formatted.append(parseStringBBcode(line))
	with open(file.rstrip('.mmd') + 'formatted.txt', 'w') as textfile:
		textfile.writelines(formatted)
			
if __name__ == '__main__':
	directory = input('Enter directory: ')
	findFiles(directory)