# ******************************************************************
#  This program is to input the details of an Address book        *
#  Author: A.AEDY                                                 *
#  C++ Date: 25 / 2/ 96 - Python Date:  30 / 12/ 22               *
#  Version 1.5   *******DOS  / Python VERSION*******              *
# ******************************************************************

import sys
import datetime
import time
from typing import List
import csv


# import the file and format to add to 'lines, dataset, number_entries' etc.
from unittest import result

first_pass = int()

if first_pass < 1:
    path = "bigdos.in"
    lines = [line for line in open(path)]

    dataset3 = []
    #   ----   try .strip to remove more from the strings later   -----
    dataset = [line.strip("  - ' \n").split(',') for line in open(path)]

    strings_set = [str(integer) for integer in dataset]
    a_string = "".join(strings_set).strip('             - \n')

    dataset2 = dataset

    for word in lines[0].split():
        if word.isdigit():
            dataset3.append(int(word))
            strings = [str(integer) for integer in dataset3]
            a_string = "".join(strings)
            loading_entries = int(a_string)
    first_pass += 1
else:
    print("First Pass = ", first_pass)



temp0 = 4
temp1 = 40
temp2 = 50
temp3 = 20
temp4 = 30
temp5 = 40
temp6 = 30

dummy4 = [temp0]
name1 = str()
address1 = str()
sex1 = str()
age1 = str()
phone1 = str()
birthday1 = str()
date_of_entry = str()

Width = 22
minval = 1
maxval = 5
total = 200

exit_p = 0
users_choice = 0
users_choice2 = 0

name = [temp1]
address = [temp2]
sex = [temp3]
age = [temp4]
phone = [temp5]
birthday = [temp6]

test_entry = {"name": 0, "address": 0, "sex": 0, "age": 0, "phone": 0, "birthday": 0}

#Address_book = [total]
Address_book = [0][0]

# **************************  FUNCTION DECLARATION'S ***********************

# ***************************  credits_f FUNC  *****************************
def credits_f():
    print(" *************************************************** ")
    print(" *              ADDRESS BOOK PROGRAM               * ")
    print(" *           ---------------------------           * ")
    print(" *                 BY AIDAN AEDY                   * ")
    print(" *           DOS REGISTERED VERSION 1.5            * ")
    print(" *            LICENSED TO - AIDAN AEDY             * ")
    print(" *************************************************** ")
    print("loading_entries ", loading_entries)
    print()


# **************************************************************************
#                            START OF MAIN FUNCTION                        *
# **************************************************************************


def main(users_choice):

    if users_choice != 5:
        print("          *** Enter Your Choice of Menu ***")
        print("            -------------------------    ")
        print("          1.| To Add An Entry.")
        print("          2.| To Delete An Entry.")
        print("          3.| To Display All Entries.")
        print("          4.| To Goto Find Menu.")
        print("          5.| To Exit From The Program. ")
        print()
        print()
        menu(users_choice, exit_p)
    else:
        print("          Thank You For Using The ADDRESS BOOK..")
        print("          You Will Now Return To DOS.")
    # fileout (number_entries)

# ***************************   END MAIN FUNC. ! **************************


'''**************************************************************************
*                            ***     NOTE'S     ***                         *
* there should be these functions included in here:                         *
* Add_f - an entry into the Address book.                                     *
* remove - an entry                                                         *
* display all entries                                                          *
* find - entry for a named person; all entries for people of same birthday  *
* all persons with age in specified range; all entries for persons of phone *
* in specified range;                                                       *
*                                                                           *
**************************************************************************'''

'''**************************************************************************
*                            START OF MAIN MENU FUNC.                       *
**************************************************************************'''


def menu(users_choice, exit_p):  # to select one of the listed func.
    number_entries = loading_entries
    print("   ---  Please Type Your Choice of Menu ---")
    print()
    users_choice = int(input())
    if users_choice == 1:
        number_entries = Add_f(loading_entries)  # dec of Add func
        main(users_choice)
    elif users_choice == 2:
        pass
        main(users_choice=0)
        #Delete()  # dec of Delete func
    elif users_choice == 3:
        Display(number_entries)  # dec of Display func
        main(users_choice=0)
    elif users_choice == 4:
        pass
        main(users_choice=0)
        #Find(users_choice2)  # dec of Find menu
    elif users_choice == 5:
        exit_p = 1
        print("          You Will Now Exit The Program")
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        main(users_choice=0)

# **********************  END MAIN MENU FUNC. *********************




'''****************************************************************
**********************    Add_f Function       ********************
****************************************************************'''


def Add_f(number_entries):
    #	system("cls")
    print("****************************************************************")
    print()
    print()
    # Global and nonlocal or returning the value through the function parameter
    groo = (number_entries + 1)

    print("          Please input the persons details for:-")
    print("          Name, ", "Address, ", "Sex, ", "Age, ")
    print("          Phone Numbers ", "and Birthday. ")
    print("          This Is Entry # ", groo, " In Your Address Book.")
    print()
    print()

    '''__________________________________________________________
    				 THIS IS THE MAIN INPUT SECTION
    __________________________________________________________'''

    # area to test new entries instead of pointers

    print("number_entries = ", number_entries)

    print("          Name             -  : ")
    name_str = input(str())
    name1 = "Name          - "
    name1 += name_str
    print("name input", name1)

    print()
    print("          Address          -  : ")
    address_str = input(str())
    address1 = "Address       - "
    address1 += address_str

    print()
    print("          Sex              -  : ")
    sex_str = input(str())
    sex1 = "Sex           - "
    sex1 += sex_str

    print()
    print("          Age              -  : ")
    age_str = input(str())
    age1 = "Age           - "
    age1 += age_str

    print()
    print("          Phone Number     -  : ")
    phone_str = input(str())
    phone1 = "Phone         - "
    phone1 += phone_str

    print()
    print("          Date of Birth    -  : ")
    birthday_str = input(str())
    birthday1 = "Date of Birth - "
    birthday1 += birthday_str

    date_of_entry_str = datetime.date.today()
    date_of_entry_str2 = time.strftime("%H:%M:%S")
    date_stamp = "Date of File  - "
    date_stamp += str(date_of_entry_str)
    date_stamp += str(" at ")
    date_stamp += str(date_of_entry_str2)

    #remove when finished testing
    print("input information etc", name1, address1, sex1, age1, phone1, birthday1, date_stamp)

    #Append each entry onto the dataset list

    dataset2.append(name1)
    dataset2.append(",")
    dataset2.append(address1)
    dataset2.append(",")
    dataset2.append(sex1)
    dataset2.append(",")
    dataset2.append(age1)
    dataset2.append(",")
    dataset2.append(phone1)
    dataset2.append(",")
    dataset2.append(birthday1)
    dataset2.append(",")
    dataset2.append(date_stamp)
    number_entries += 1
    num_temp_entries = str(number_entries)
    num_temp_entries += "             - # of Entries."
    dataset2[0] = num_temp_entries
    print("number_entries", number_entries)
    print("          You will now return to the MAIN MENU. ")
    print("dataset2", dataset2)
    print("number_entries", number_entries)
    return number_entries
    #main(users_choice)




    # *****        END Add_f FUNC.    *****


''' this was Added to remove all but the basic functions() and I will change as I get things working'''

'''

def Delete():
#	int s
#	int loo

    dummy[50]
    find[50]

    print()
    input("Please Enter The Person's Name,")
    print()
    input(" Of The File You Want To Delete - ")
    input(find)

    strcpy (findupr, find)
    _strupr(findupr)
    for  (s=0s<=totals++)


    if (!strcmp(findupr, Address_book[s].name))  

        loo = s


    for (loo<=number_entriesloo++)		

        strcpy (Address_book[loo].name, dummy)
        strcpy (Address_book[loo].Address, dummy)
        strcpy (Address_book[loo].sex, dummy)
        strcpy (Address_book[loo].age, dummy)
        strcpy (Address_book[loo].phone, dummy)
        strcpy (Address_book[loo].birthday, dummy)
        int p=loo+1

        strcpy (Address_book[loo].name, Address_book[p].name)
        strcpy (Address_book[loo].Address, Address_book[p].Address)
        strcpy (Address_book[loo].sex, Address_book[p].sex)
        strcpy (Address_book[loo].age, Address_book[p].age)
        strcpy (Address_book[loo].phone, Address_book[p].phone)
        strcpy (Address_book[loo].birthday, Address_book[p].birthday)

    if (loo=s)

        number_entries--
        fputs("-- The File Is Now Erased --", stdout)


    if (loo!=s)

        fputs( "----- There Were No Files Deleted -----", stdout) 


    fputs( "You Are Now Returning To The Main Menu.", stdout)

#     ************ end of delete func. ***************

'''

# ************************************************************************
# ********************  Display Function   *******************************
# ************************************************************************

def Display (number_entries):
    poo = 0
    sloo = 0
    poo += 1
    dummy = "y"
    print("          ***   This is the ", sloo+1, "of ", number_entries, " enties stored in the data base.   ***")

    while sloo < number_entries:
        #while dummy != "n":
        print("          Name          - ", dataset2[poo])
        print("          Address       - ", dataset2[poo+1])
        print("          Sex           - ", dataset2[poo+2])
        print("          Age           - ", dataset2[poo+3])
        print("          Phone         - ", dataset2[poo+4])
        print("          Date of Birth - ", dataset2[poo+5])
        print("          Date of Entry - ", dataset2[poo+6])
        print("     Entry Number: ", sloo+1, "     ...Are you ready for Another ?...")
        input(str(dummy))
        sloo += 1
        poo += 7
    else:
        print()
        print("          That was the last Entry.......")
        print("          You will now return to the MAIN MENU. ")
        poo = 0
        print()
    return number_entries
    print()
   

# ***********************    END DISPLAY FUNC.   **********************





# ************************************************************************
# ********************  Calling Functions  *******************************
# ************************************************************************




credits_f()

main(users_choice)




'''

/*************************************************************************
*                                                                        *
*                           START OF FIND MENU FUNC.                     *
*                                                                        *
*************************************************************************/
 void Find (int users_choice2)
 
  {
	system("cls");	
	cout << endl << endl
		 << "*** Enter The Type Of Find You Require ***" << endl 
		 << "    ----------------------------------    " << endl << endl
		 << "1.| To Find A Named Entry." << endl << endl
		 << "2.| To Find Persons with A Particular Birthday." << endl << endl
		 << "3.| To Find Persons in An Age Range." << endl << endl
		 << "4.| To Find Persons With A Phone Number." << endl << endl
		 << "5.| To Exit From The Find Menu. " << endl << endl;

	cout << endl << "Your Choice of Find Menu is:- #";
	cin  >> users_choice2;
	cout << endl << endl;

		 switch (users_choice2)
	   { 
				
		   case 1:
				Named ();     //dec of Named func
				break;
				
		   case 2:
				Birthday ();  //dec of Birthday func
				break; 
		  
		   case 3:
				Age_range (); //dec of Age func
				break;

		   case 4:
				Phone ();
				break;
				
		   case 5:
				cout << " You are now going to exit the find menu ";
				break;
				
		   default:  cout << "You Have Made An Incorrect Choice" << endl;	 
	   }
 
	  system("cls");
  }//************************  END FIND MENU. *************************




/**********************************************************************
*                         START OF NAMED PERSON FUNC.                 *
**********************************************************************/

 void Named (void) 
 {  
	int s;
	int flew;
	char dummy [1];
	char find[50];
	char findupr[50];
		
		system("cls");
		fputs("Please Enter The Persons Name To Search For -  ",stdout);
		gets(find);
			
		strcpy (findupr, find);
		_strupr(findupr);
		for  (s=0;s<=number_entries;s++)
		   {
			 
			  if (!strcmp(findupr, Address_book[s].name))  
				{
					 cout << endl 
						  << endl << Address_book[s].name 
						  << endl << Address_book[s].Address
						  << endl << Address_book[s].sex 
						  << endl << Address_book[s].age 
						  << endl << Address_book[s].phone
						  << endl << Address_book[s].birthday
						  << endl << endl;                       
					  flew = 1;
				}
		   
		  }   
	  if (flew!=1)
		{
			cout << "There Were No Files Of That Name Found " << endl;
		}
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
			
 }/***********************  END FIND NAME FUNC.  ***********************/



/************************************************************************
*                         START OF BIRTHDAY FUNC.                       *
************************************************************************/
  
 void Birthday (void)
 {
	int s;
	char dummy [1];
	char find[50];
	char findupr[50];
		
		system("cls");	
		fputs("Please Enter The Persons Birthday To Search For -  ",stdout);
		gets(find);
			
		strcpy (findupr, find);
		_strupr(findupr);
		for  (s=0;s<=number_entries;s++)
		   {
			 
			  if (!strcmp(findupr, Address_book[s].birthday))  
				{
					 cout << endl 
						  << endl << Address_book[s].name 
						  << endl << Address_book[s].Address
						  << endl << Address_book[s].sex 
						  << endl << Address_book[s].age 
						  << endl << Address_book[s].phone
						  << endl << Address_book[s].birthday
						  << endl << endl;                       
				}
		   
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
 
 } //**********************  END OF BIRTHDAY FUNC. **********************
 
 
 
/************************************************************************
*                           START OF AGE RANGE FUNC.                    *
************************************************************************/
 
 void Age_range (void)
 {
	int s;
	char dummy [1];
	char find1[50];
	char find2[50];
	char findupr1[50];
	char findupr2[50];	
		system("cls");
		fputs("Please Enter The Age Range To Search For -  ",stdout);
		cout << endl;
		fputs("From ( lowest  # ) - ", stdout);
		gets(find1);
		cout << endl;
		fputs("To   ( highest # ) - ", stdout);
		gets(find2);
		cout << endl;
		strcpy (findupr1, find1);
		_strupr(findupr1);
		strcpy (findupr2, find2);
		_strupr(findupr2);

		for  (s=0;s<=number_entries;s++)
		  {
			 
		   if (strcmp(findupr1, Address_book[s].age)<0) 
			{
			
			 if (strcmp(findupr2, Address_book[s].age)>0) 
				{
					cout << endl 
						 << endl << "Name    - " << Address_book[s].name 
						 << endl << "Address - " << Address_book[s].Address
						 << endl << "Sex     - " << Address_book[s].sex 
						 << endl << "Age     - " << Address_book[s].age 
						 << endl << "Phone   - " << Address_book[s].phone
						 << endl << "Birthday- " << Address_book[s].birthday
						 << endl <<  endl;                       
				}
		   
		   
			}
		  
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
  
 }//****************      END OF AGE RANGE FUNC.     **************** 



 
 /*******************************************************************
  *                     START OF PHONE # FUNC.                 *
  *******************************************************************/
 
 void Phone (void)
 {
	int s;
	char dummy [1];
	char find1[50];
	char findupr1[50];
		system("cls");	
		fputs("Please Enter The Phone Number To Search For -  ",stdout);
		cout << endl;
		fputs(" - ", stdout);
		gets(find1);
		cout << endl;
		strcpy (findupr1, find1);
		_strupr(findupr1);

		for  (s=0;s<=number_entries;s++)
		  {
			 
		   if (!strcmp(findupr1, Address_book[s].phone)) 
			{
			
			 if (!strcmp(findupr1, Address_book[s].phone)) 
				{
					cout << endl 
						 << endl << "Name    - " << Address_book[s].name 
						 << endl << "Address - " << Address_book[s].Address
						 << endl << "Sex     - " << Address_book[s].sex 
						 << endl << "Age     - " << Address_book[s].age 
						 << endl << "Phone   - " << Address_book[s].phone
						 << endl << "Birthday- " << Address_book[s].birthday
						 << endl <<  endl;                       
				}
		   
		   
			}
		  
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
 }    /************  END OF  HEIGHT RANGE FUNC. *****************/
 





		  

	
/*****************************************************************
*                         START OF FILE OUT FUNC                 *
*****************************************************************/
   
  void fileout (int &number_entries) 
  
	 { 
	
	ofstream g("\\BIGDOS.INI",ios::trunc,filebuf::openprot);
   
   int poo;
		g << number_entries << "             - # of Entries.";
   
   for (poo=0;poo<number_entries;poo++)
	{	
		
		g << endl << "Name          - " << Address_book[poo].name;

		g << endl << "Address       - " << Address_book[poo].Address;

		g << endl << "Sex           - " << Address_book[poo].sex;

		g << endl << "Age           - " << Address_book[poo].age;
		
		g << endl << "Phone         - " << Address_book[poo].phone;

		g << endl << "Date of Birth - " << Address_book[poo].birthday;
		
	}
} //***********************    END File Out FUNC.   ********************** 

'''



