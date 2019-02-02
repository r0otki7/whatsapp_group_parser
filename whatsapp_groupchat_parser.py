from collections import Counter
import re

#Some Global Variables
keywords = ['added', 'removed', 'changed', 'left', 'joined', 'group']
nums = {'Contact Name': 'Contact Number', 'Contact Name2': 'Contact Number2' } #According to what you've saved in your contact list, add all the contacts in this dictionary

def main():
	file_ops('<filename>.txt', '(\d\d)/01/19')	#Replace <filename> with the whatsapp chat export filename, and a particular date to get messages from that date(regex supported).
	dump('total_count.txt', number_engine('replaced_chat.txt'))
	dump('this_month_count.txt', number_engine('month.txt'))
	one_count('total_count.txt')
	inactive_contacts('all_contacts.txt', 'total_count.txt')

#Open the file and create a backup with replaced contacts, and a file for this month's messages
def file_ops(filename, date):
	with open(filename, 'r') as f:
		file_replace = f.read()
	for k, v in nums.items():
		file_replace = file_replace.replace(k, v)
	with open('replaced_chat.txt', 'w') as f:
		f.write(file_replace)
	with open('month.txt', 'w') as f:
		f.write(re.split(r'{0}'.format(date), file_replace, 1)[2])

#Parsing the replaced_chat.txt for number of messages
def number_engine(filename):
	number = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			if re.match(r'^(\d\d)/(\d\d)/(\d\d)', line):
				data = line.split('-')
				if len(data) > 1:
					num = data[1].split(':')[0]
				if any(kwords in num for kwords in keywords):
					continue
				number.append(num.translate(None, '\xe2\x80\xaa\xac'))
	return number
	
#Writing numbers to a file
def dump(filename, number):
	with open(filename, 'w') as f:
		for key, count in Counter(number).most_common():
			f.write('{} : {}'.format(key, count)+"\n")

#To find out people with only 1 message count, configurable
def one_count(filename):
	onemessage = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			#Matching the output format for the line beginning
			if re.match(r'^ \+(\d)', line):
				#Checking for people with one message
				if line.split(':')[1].strip() == '1':		#Change the number here to see members with certain number of messages
					#Now checking in the original file, and dumping the messages
					with open('replaced_chat.txt', 'r') as f1:
						for line1 in f1.readlines():
							#Matching for the valid line
							if re.match(r'^(\d\d)/(\d\d)/(\d\d)', line1):
								if line.split(':')[0].strip() in line1.strip():
									if any(kwords in line1 for kwords in keywords):
										continue
									onemessage.append(str(line1))
	with open('onemessage.txt', 'w') as f:
		for l in onemessage:
			f.write(l)

#To find out those with 0 message count, need an input file with all the contact numbers in each line			
def inactive_contacts(allfile, activefile):
	allcontacts = []
	activecontacts = []
	with open(allfile, 'r') as f:
		for line in f.readlines():
			allcontacts.append(line.strip('\n'))
	with open(activefile, 'r') as f:
		for line in f.readlines():
			activecontacts.append(line.split(':')[0].strip())
	with open('inactive_contacts.txt', 'w') as f:
		for i in list(set(allcontacts) - set(activecontacts)):
			f.write(i + '\n')
		
if __name__ == '__main__':
	main()