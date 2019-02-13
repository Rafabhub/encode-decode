'''#############################################################

			Created by: 	Rafael Breno Rocha Reis

#############################################################'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def convertStringToList(content):
	_List = []
	for i in range(len(content)):
		_List.append(content[i])
	return _List

def convertListToString(content):
	return ''.join(content)

def getLastElement(content):
	return content[len(content)-1][:]

def toEncode(content):
	elements_list = []
	element = convertStringToList(content)
	elements_list.append(element)
	
	for i in range(len(content)-1):
		currentElement = getLastElement(elements_list)
		caracter = getLastElement(currentElement)
		currentElement.pop()
		currentElement.insert(0,caracter)
		elements_list.append(currentElement)
	return elements_list

def getLastWords(content, word):
	out = []
	cont = 0
	for i in content:
		out.append(i[len(word)-1][:])
	return out

def getLine(content, word):
	out = convertStringToList(word)
	count = 0
	for i in content:
		if(out == i):
			return count
		else:
			count = count + 1

def convertOutputEncode(content, word):
	outWord = convertListToString(getLastWords(content,word))
	outLine = getLine(content,word)
	output  = '[\'' + outWord + '\', ' + str(outLine) + ']'
	return output

def toDecode(content):
	word_List = convertStringToList(content)
	add = word_List[:]

	for i in range(len(word_List)-1):
		add = sorted(add)
		for j in range(len(word_List)):
			add[j] = word_List[j] + add[j]

	add = sorted(add)
	return add

def convertOutputDecode(content, number):
	return content[int(number)]	



param = sys.argv[1:]

if("encode" in param[0]):
	#####Open file#####
	file = open(param[0], 'r') 
	content_file = file.read()
	file.close()
	###################


	########Removing trashes#########
	content_file = content_file.replace('\n','') #Remove the \n trash
	#################################

	elements = sorted(toEncode(content_file))
	
	outputName = param[0].split('.')
	outputName = outputName[0] + '.out'

	file = open(outputName,'w')
	output = convertOutputEncode(elements, content_file)
	file.write(output)
	file.close()


elif("decode" in param[0]):
	file = open(param[0], 'r')
	content_file = file.read()
	file.close()
	########Removing trashes#########
	content_file = content_file.replace('\'','')
	content_file = content_file.replace('[','')
	content_file = content_file.replace(']','')
	content_file = content_file.split(',')
	###############################
	numberLine = content_file[1].replace(' ','')
	word_List = convertStringToList(content_file[0])

	matrixDecode = toDecode(word_List)

	outputName = param[0].split('.')
	outputName = outputName[0] + '.out'

	file = open(outputName,'w')
	output = convertOutputDecode(matrixDecode, numberLine)
	file.write(output)
	file.close()


