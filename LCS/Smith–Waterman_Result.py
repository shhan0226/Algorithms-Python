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

num_cutoff = 50

Query=""
Database=""
width = MAX_result = start_x =start_y = 0
LCS_MAT = []


Query_ ={}
Database_={}
Query_ID =""
Database_ID =""


def READ():
        global Query_, Database_, Query_ID, Database_ID

        if len(sys.argv) != 3:
                print "Command error : file.py [Query] [Database]"
                sys.exit()


        in_file = sys.argv[1]
        fp = open(in_file, "r")

        in_file2 = sys.argv[2]
        fp2 = open(in_file2, "r")


        for lineStr in fp:
                tmp_str = str(lineStr)
                if ">" == tmp_str[0]:
                        Query_ID = tmp_str[1:-1]
                        Query_[ Query_ID ] = ""
                else:
                        Query_[ Query_ID ] = Query_[ Query_ID ] + tmp_str[:-1]

        for lineStr2 in fp2:
                tmp_str = str(lineStr2)
                if ">" == tmp_str[0]:
                        Database_ID = tmp_str[1:-1]
                        Database_[ Database_ID ] =  ""
                else:
                        Database_[ Database_ID ] = Database_[ Database_ID ] + tmp_str[:-1]
#	print Query_
#	print Database_
	


def INIT():
	global Query, Database, LCS_MAT, width, MAX_result, start_x, start_y, Query_, Database_
	LCS_MAT = []
	width = MAX_result = start_x =start_y = 0

	for Q in Query_.keys():
		for D in Database_.keys():
			Query = " "+str(Query_[Q])
			Database = " "+str(Database_[D])
			print "\n> Qeury    |name: ",Q
			print Query
			print "\n  Database |name: ",D
			print Database
			width = len(Query)	
			LCS_MAT = [0]*(width*len(Database))
			LCS_CONSIT()
		





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
				
#	print PRINT_MAT()
	MAX_VALUE()
	

	
	
def MAX_VALUE():	
	global Query, Database, LCS_MAT, width, MAX_result, start_x , start_y
	MAX_result = start_x = start_y =0
	print "\n[VALUE]"
	for x in range(1, len(Query)):
		for y in range(1, len(Database)):
			if MAX_result < LCS_MAT[x+y*width]:
				start_x =x
				start_y =y
				MAX_result = LCS_MAT[x+y*width]

	print "x =",start_x,"/ y =",start_y,"/ Match_score =",MAX_result,
	BACK_TRACE()


def BACK_TRACE():
	global Query, Database, LCS_MAT, width, start_x, start_y, MAX_result, num_cutoff
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
		if LCS_MAT[ (Query_x-1) + Database_y * width ] >= LCS_MAT[ Query_x + (Database_y-1) * width ]:
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

	size = len(Result_Q)
	i=1
	MAX_range=j=k=l= 0

	print "/ LCS_string =",size
	print "\n[Result]"

	if size < num_cutoff:
		for j in range(j , size):
			print Result_Q[j],
		print ""
		for k in range(k , size):
			print Match_seq[k],
		print ""
		for l in range(l , size):
			print Result_D[l],
		print ""

	else:
		share = size / num_cutoff
		remainder = size % num_cutoff

		while(i <= share ):
			MAX_range = num_cutoff * i
			for j in range(j , MAX_range):
				print Result_Q[j],
			print ""
			for k in range(k , MAX_range):
				print Match_seq[k],
			print ""
			for l in range(l , MAX_range):
				print Result_D[l],
			print ""
			print ""
			i = i + 1
			j = k = l = MAX_range
	
		
		for j in range(j , MAX_range + remainder):
			print Result_Q[j],
		print ""
		for k in range(k , MAX_range + remainder):
			print Match_seq[k],
		print ""
		for l in range(l , MAX_range + remainder):
			print Result_D[l],
		print ""

		

		
#	sub_max = size %  50
	blanks_str = "_"*num_cutoff
	print blanks_str+blanks_str
	
		


	
if __name__ == '__main__':


	READ()
	INIT()
