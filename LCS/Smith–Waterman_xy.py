#!/usr/bin/python
# -*- coding:utf-8 -*-

# made in Seok-hyeon Han

import sys
import os
import re
import commands

MATCH = 2
MISMATCH = -1
GAP = -1


Query=""
Database=""
width = MAX_result = start_x =start_y = 0
LCS_MAT = []

def INIT():
	global Query, Database, LCS_MAT, width

	Query = " "+"AAGAAGCCGG"
	Database =" "+"GAAGGCCT"
	width = len(Query)
	
	LCS_MAT = [0]*(width*len(Database))
	print "> Query :",Query
	print "Database:",Database
	print "\n",
#	print LCS_MAT

#	num1 =1
#	num2 =2
#	num = num1 if num1>num2 else num2
#	print num


def PRINT_MAT():
	global LCS_MAT, Query, Database, width
	print "[MATRIX]"

	print "[@] ",
	for i in range(0, len(Query)):
		print Query[i],", ",
	print "...Query"
	
	
	i=0
	j=0
	print Database[j],"| ",
	for data in LCS_MAT:
		if i == width-1:
			i=0
			print data
			j = j+ 1
			if j < len(Database):
				print Database[j],"| ",
		else:
			print data,", ",
			i = i + 1
	print "...Database"
	
		
		

def LCS_CONSIT():
	global Query, Database, LCS_MAT, width, MATCH, GAP
	for x in range(1, len(Query)):
		for y in range(1, len(Database)):
#			print "x:",x," y:",y
			weight = 0
			Deletion = 0
			if(Query[x] == Database[y]):
				weight = weight if weight >  LCS_MAT[(x-1)+(y-1)*width] + MATCH else LCS_MAT[(x-1)+(y-1)*width] + MATCH
				Deletion = LCS_MAT[(x-1)+y*width]+GAP if LCS_MAT[(x-1)+y*width]+GAP > LCS_MAT[x+(y-1)*width]+GAP else LCS_MAT[x+(y-1)*width]+GAP
				weight = weight if weight > Deletion else Deletion
				LCS_MAT[x+y*width] = weight 

			else:
				weight = weight if weight >  LCS_MAT[(x-1)+(y-1)*width] + MISMATCH else LCS_MAT[(x-1)+(y-1)*width] + MISMATCH
				Deletion = LCS_MAT[(x-1)+y*width]+GAP if LCS_MAT[(x-1)+y*width]+GAP > LCS_MAT[x+(y-1)*width]+GAP else LCS_MAT[x+(y-1)*width]+GAP
				weight = weight if weight > Deletion else Deletion
				LCS_MAT[x+y*width] = weight 
				
#	print LCS_MAT
	

	
	
def MAX_VALUE():	
	global Query, Database, LCS_MAT, width, MAX_result, start_x , start_y 
	print "\n[MAX VALUE]"
	for x in range(1, len(Query)):
		for y in range(1, len(Database)):
			if MAX_result < LCS_MAT[x+y*width]:
				start_x =x
				start_y =y
				MAX_result = LCS_MAT[x+y*width]

	print "x: ",start_x," y: ",start_y," Max: ",MAX_result


def BACK_TRACE():
	global Query, Database, LCS_MAT, width
#	Result = Query[1]
#	print Result
#	Result = Result + Query[2]
#	print Result
	Result_Q = ""
	Result_D = ""
	Match_seq = ""

	Query_x = start_x
	Database_y = start_y

	while Query_x > 0 and Database_y > 0:
		if LCS_MAT[(Query_x-1)+ Database_y*width] >= LCS_MAT[Query_x+( Database_y-1) *width]:
			if LCS_MAT[(Query_x-1)+(Database_y-1)*width] >= LCS_MAT[(Query_x-1)+Database_y*width]:
				Match_seq = Match_seq + "|"
				Result_Q = Result_Q + Query[Query_x]
				Result_D = Result_D + Database[Database_y] 
				Query_x = Query_x-1
				Database_y = Database_y-1
				
				
			else:
				Match_seq = Match_seq + " "
				Result_Q = Result_Q + Query[Query_x]
				Result_D = Result_D + "-"
				Query_x = Query_x-1
#				Database_y = Database_y-1
				

		else:
			if LCS_MAT[(Query_x-1)+(Database_y-1)*width] >= LCS_MAT[Query_x+(Database_y-1)*width]:
				Match_seq = Match_seq + "|"
				Result_Q = Result_Q + Query[Query_x]
				Result_D = Result_D + Database[Database_y] 
				Query_x = Query_x-1
				Database_y = Database_y-1
	

			else:
				Match_seq = Match_seq + " "
				Result_D = Result_D + Database[Database_y]
				Result_Q = Result_Q + "-"
				Database_y = Database_y-1
#				Query_x = Query_x-1

	Result_Q = Result_Q[::-1]
	Match_seq = Match_seq[::-1]
	Result_D = Result_D[::-1]
	print "\n[Result]"
	print Result_Q
	print Match_seq
	print Result_D
	
		


	
if __name__ == '__main__':

	INIT()
	LCS_CONSIT()
	PRINT_MAT()
	MAX_VALUE()
	BACK_TRACE()
