/******************************************************************
*  This program is to input the details of an address book        * 
*  Author: A.AEDY                                                 *
*  Date: 25 / 2/ 96                                               *
*  Version 1.5   *******DOS VERSION*******                        *
******************************************************************/

 #include <iostream.h>
 #include <iomanip.h>  // setw() etc.
 #include <string.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <fstream.h>
 #pragma  warning(disable:4270) 
  
 
 const unsigned temp0 = 4;
 const unsigned temp1 =40;
 const unsigned temp2 =50;
 const unsigned temp3 =20;
 const unsigned temp4 =30;
 const unsigned temp5 =40;
 const unsigned temp6 =30;



  	 char  dummy4    [temp0];
	 char  name1     [temp1];
  	 char  address1  [temp2];
  	 char  sex1      [temp3];
  	 char  age1      [temp4];
  	 char  phone1    [temp5];
  	 char  birthday1 [temp6];

 const int Width  = 22;
 const int minval = 1;
 const int maxval = 5;
 const int total  = 200;     
 
 
 	   int count;  
	   int users_choice;
	   int users_choice2;

 	   
struct book
{
   char  name     [temp1];
   char  address  [temp2];
   char  sex      [temp4];
   char  age      [temp3];
   char  phone    [temp5];
   char  birthday [temp6];
   
}address_book [total]; 


 /**********************  FUNCTION DECLARATION'S ****************/
 
 void menu(int users_choice, int &exit);//pre dec of Menu func  
 
 void Add (int &count);                 //pre dec of Add func.
                       
 void Delete (void);                    //pre dec of Delete func                      
 		   
 void Display (int &count);             //pre dec of Display func. 
 
 void Find (int users_choice2);         //pre dec of Find menu 
 
 void Named (void);                     //pre dec of Find menu Named func
 
 void Birthday (void);                  //pre dec of Find menu Birthday func
 
 void Age_range (void);                 //pre dec of Find menu Age_range func
 
 void Phone (void);                     //pre dec of Find menu Phone func
 
 void filein (int &count);              //pre dec of Read From File func. 
 
 void fileout (int &count);             //pre dec of write to File func. 
  
 void credits (void);                   //pre dec of credits screen func.
  
 /**************************************************************************
 *                           START OF MAIN FUNCTION                        *
 **************************************************************************/
 
 
 void main (int users_choice)
 {  

  int exit;
  filein (count);    
  credits ();
   do
   	{ 
				cout << endl << endl
					 << "*** Enter Your Choice of Menu ***" << endl 
					 << "    -------------------------    " << endl << endl
          			 << "1.| To Add An Entry." << endl << endl
          			 << "2.| To Delete An Entry." << endl << endl
          			 << "3.| To Display All Entries." << endl << endl
          			 << "4.| To Goto Find Menu." << endl << endl
          	         << "5.| To Exit From The Program. " << endl << endl;
          	         
				menu(users_choice, exit);
      
   	}  
  while (exit != 1);
  system("cls");
  cout << "Thank You For Using The ADDRESS BOOK.."
  	   << endl << "You Will Now Return To DOS."	;
  fileout (count); 	

    
} //**************************   END MAIN FUNC. ! **************************





/****************************************************************************
*                            ***     NOTE'S     ***                         *
* there should be these functions included in here:                         *
* Add - an entry into the adress book.                                      *
* remove - an entry                                                         *
* display an entry                                                          *
* find - entry for a named person; all entries for people of same birthday ;*
* all persons with age in specified range; all entries for persons of phone*
* in specified range;                                                       *
*                                                                           *
****************************************************************************/

/****************************************************************************
*                            START OF MAIN MENU FUNC.                       *
****************************************************************************/
 void menu(int users_choice, int &exit) // to select one of the listed func.
  
  {            
     
				cout << endl << "Your Choice of Menu is:- #";
				cin  >> users_choice;
				cout << endl << endl;


         switch (users_choice)
       { 
          		
           case 1:
				Add (count);          //dec of Add func
                break;
                
           case 2:
				Delete ();            //dec of Delete func
                break;
		   
		   
		   case 3:
                		   		
				Display ( count);      //dec of Display func
          	    break; 
          
           case 4:
          	    Find (users_choice2); //dec of Find menu
          	    break;
          	    
           case 5:
            	exit = 1;
          	    break;
          	    
           default:  cout << "You Have Made An Incorrect Choice" << endl;	 
         
       }
  
  
  
  }//**********************  END MAIN MENU FUNC. *********************




      /****************************************************************
      **********************    Add Function       ********************
      ****************************************************************/
                                   
 void Add (int &count)
       
  	{ 
      system("cls");  	
  	  cout << "********************************************************" 
  	    	 << endl << endl;
      int groo;
    
      groo=(count+1);
       
      cout << setw(Width) <<"Please input the persons details for:-" ;
      cout << endl << endl << "Name, " << "Address, " << "Sex, " << "Age, "; 
	  cout << "Phone Numbers " << "and Birthday. " << endl << endl; 
      cout << "This Is Entry # " << groo << " In Your Address Book." <<endl <<endl;
       
       /*__________________________________________________________
                     THIS IS THE MAIN INPUT SECTION
         __________________________________________________________*/              
            
			fputs( " Name             -  : ",stdout);
            gets(name1);
			strcpy (address_book[count].name, name1);
			_strupr(address_book[count].name);
    
  		    
  		    cout << endl ;
  		    fputs( " Address          -  : ", stdout);
  		    //cin.getline(address1, temp2);//example of what didn't work....   
  		    gets(address1); 
    		strcpy (address_book[count].address, address1);
            //DO NOT CONVERT THE E-MAIL ADDRESS AS IT IS CASE SENSITIVE !
            			
			cout << endl ;
			fputs( " Sex              -  : ", stdout);
			gets(sex1);
			strcpy (address_book[count].sex, sex1);
	   		_strupr(address_book[count].sex);

		    
		    cout << endl ;
		    fputs( " Age              -  : ", stdout);
   			gets(age1);
   			strcpy (address_book[count].age, age1);
   			_strupr(address_book[count].age);

            
            cout << endl ;
            fputs( " Phone Number     -  : ", stdout);
   			gets(phone1);
   			strcpy (address_book[count].phone, phone1);
   			_strupr(address_book[count].phone);

            
            cout << endl; 
            fputs( " Date of Birth    -  : ", stdout);
	   		gets(birthday1);
	   		strcpy (address_book[count].birthday, birthday1);
   			_strupr(address_book[count].birthday);

   			cout << endl << endl
   				 << "You will now return to the MAIN MENU. " 
   				 << endl << endl << endl; 	
            system("cls");
  	    count++;
  	} // *****        END ADD FUNC.    ***** 
  	

 void Delete (void)
 {

    int s;
    int loo;
    
    char dummy[50];
    char find[50];
	char findupr[50];
		
	  system("cls");	
	  fputs("Please Enter The Person's Name,", stdout);
	  cout << endl;
	  fputs(" Of The File You Want To Delete - ",stdout);
      gets(find);
			
	  strcpy (findupr, find);
	  _strupr(findupr);
      for  (s=0;s<=total;s++)
       {
             
         if (!strcmp(findupr, address_book[s].name))  
            {
              loo = s;
            }
	   }	 	
	  for (;loo<=count;loo++)		
        {
		  strcpy (address_book[loo].name, dummy);
 		  strcpy (address_book[loo].address, dummy);
 		  strcpy (address_book[loo].sex, dummy);
  		  strcpy (address_book[loo].age, dummy);
  		  strcpy (address_book[loo].phone, dummy);
  		  strcpy (address_book[loo].birthday, dummy);
	      int p=loo+1;
	  
		  strcpy (address_book[loo].name, address_book[p].name);
 		  strcpy (address_book[loo].address, address_book[p].address);
 		  strcpy (address_book[loo].sex, address_book[p].sex);
  		  strcpy (address_book[loo].age, address_book[p].age);
  		  strcpy (address_book[loo].phone, address_book[p].phone);
  		  strcpy (address_book[loo].birthday, address_book[p].birthday);
       
        }      
       if (loo=s)
       	{        
         	count--;
    		fputs("-- The File Is Now Erased --", stdout);
	         	
        }
       if (loo!=s)
        {
        	fputs( "----- There Were No Files Deleted -----", stdout) ;
        }
    
    fputs( "You Are Now Returning To The Main Menu.", stdout);

}//************* end of delete func. ***************



   /*********************************************************************
   **************  Display Function   ***********************************
   *********************************************************************/
            
 void Display (int &count) 
   {
    
   system("cls");
   cout << "***   This is the First of your Address's stored.   ***" << endl;
   
   char dummy [1];
   
   int poo;
   
   for (poo=0;poo<count;poo++)
    {	
   		cout << endl << "Name          - " << address_book[poo].name;

   		cout << endl << "Address       - " << address_book[poo].address;

   		cout << endl << "Sex           - " << address_book[poo].sex;

   		cout << endl << "Age           - " << address_book[poo].age;
   		
   		cout << endl << "Phone         - " << address_book[poo].phone;

   		cout << endl << "Date of Birth - " << address_book[poo].birthday;

        cout << endl << endl << ".......Are you ready for Another ?.......";
        cin >> dummy[1];
        system("cls");

    }
   cout << endl << endl << "That was the last Entry......." << endl << endl;
   cout << "You will now return to the MAIN MENU. " << endl << endl << endl; 	
   

} //***********************    END DISPLAY FUNC.   **********************


      

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
        for  (s=0;s<=count;s++)
           {
             
              if (!strcmp(findupr, address_book[s].name))  
                {
              	     cout << endl 
              	     	  << endl << address_book[s].name 
                	 	  << endl << address_book[s].address
                	 	  << endl << address_book[s].sex 
                	 	  << endl << address_book[s].age 
                	 	  << endl << address_book[s].phone
                	 	  << endl << address_book[s].birthday
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
        for  (s=0;s<=count;s++)
           {
             
              if (!strcmp(findupr, address_book[s].birthday))  
                {
              	     cout << endl 
              	     	  << endl << address_book[s].name 
                	 	  << endl << address_book[s].address
                	 	  << endl << address_book[s].sex 
                	 	  << endl << address_book[s].age 
                	 	  << endl << address_book[s].phone
                	 	  << endl << address_book[s].birthday
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

        for  (s=0;s<=count;s++)
          {
             
           if (strcmp(findupr1, address_book[s].age)<0) 
            {
            
           	 if (strcmp(findupr2, address_book[s].age)>0) 
                {
                	cout << endl 
            	    	 << endl << "Name    - " << address_book[s].name 
                	 	 << endl << "Address - " << address_book[s].address
                	 	 << endl << "Sex     - " << address_book[s].sex 
                	 	 << endl << "Age     - " << address_book[s].age 
                	 	 << endl << "Phone   - " << address_book[s].phone
                	 	 << endl << "Birthday- " << address_book[s].birthday
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

        for  (s=0;s<=count;s++)
          {
             
           if (!strcmp(findupr1, address_book[s].phone)) 
            {
            
           	 if (!strcmp(findupr1, address_book[s].phone)) 
                {
                	cout << endl 
            	    	 << endl << "Name    - " << address_book[s].name 
                	 	 << endl << "Address - " << address_book[s].address
                	 	 << endl << "Sex     - " << address_book[s].sex 
                	 	 << endl << "Age     - " << address_book[s].age 
                	 	 << endl << "Phone   - " << address_book[s].phone
                	 	 << endl << "Birthday- " << address_book[s].birthday
                 		 << endl <<  endl;                       
                }
           
           
            }
          
          }   
    
    cout << "***---------- Are You Ready To Continue ? -----------***";
    cin >> dummy[1];
    system("cls");
 
 }    /************  END OF  HEIGHT RANGE FUNC. *****************/
 
          
          
  //******************************************************************       
          
  /***********************     FILE INPUT START     *****************/        
       
  //******************************************************************     
          
 void filein (int &count)    //ifstream&z                                                            
  {                  
       int dummy5;	   
       fstream z;
       z.open("\\BIGDOS.INI",ios::in);// open file for input.
       z >> dummy5; // to input the number of records in file.
       if (dummy5 >1)  // if there are any entries then input them.
       {
       z.getline (dummy4, temp1+10); // to correct error in input.
    
         do { 
         	
            z.getline( name1, temp1);
			strcpy (address_book[count].name, name1+16);
			_strupr(address_book[count].name);
    
  		    
  		    z.getline(address1, temp2);   
    		strcpy (address_book[count].address, address1+16);
            //DO NOT CONVERT THE E-MAIL ADDRESS AS IT IS CASE SENSITIVE !
            			
		    z.getline(sex1, temp3);
			strcpy (address_book[count].sex, sex1+16);
	   		_strupr(address_book[count].sex);

		    
            z.getline( age1, temp4);
   			strcpy (address_book[count].age, age1+16);
   			_strupr(address_book[count].age);

            
            z.getline( phone1, temp5);
   			strcpy (address_book[count].phone, phone1+16);
   			_strupr(address_book[count].phone);

            
            z.getline( birthday1, temp6);
	   		strcpy (address_book[count].birthday, birthday1+16);
   			_strupr(address_book[count].birthday);

  	        count++;
            
            
   	    }
        while (count<dummy5); 
      }
  
  } /***************************************************************
    *                                                              *
    *                      END FILE IN FUNC.                       *
    ***************************************************************/
   
    
    
    
   /*****************************************************************
   *                         START OF FILE OUT FUNC                 *
   *****************************************************************/
   
  void fileout (int &count) 
  
     { 
    
    ofstream g("\\BIGDOS.INI",ios::trunc,filebuf::openprot);
   
   int poo;
   		g << count << "             - # of Entries.";
   
   for (poo=0;poo<count;poo++)
    {	
   		
   		g << endl << "Name          - " << address_book[poo].name;

   		g << endl << "Address       - " << address_book[poo].address;

   		g << endl << "Sex           - " << address_book[poo].sex;

   		g << endl << "Age           - " << address_book[poo].age;
   		
   		g << endl << "Phone         - " << address_book[poo].phone;

   		g << endl << "Date of Birth - " << address_book[poo].birthday;
        
    }
} //***********************    END File Out FUNC.   ********************** 

                                                                          
                                                                          
                                                                          
                                                                          
//***************************  CREDITS FUNC  *****************************
void credits ()
{   
	system("cls");
	cout << " *************************************************** " << endl
		 << " *           E-MAIL ADDRESS BOOK PROGRAM           * " << endl
         << " *           ---------------------------           * " << endl
		 << " *                 BY AIDAN AEDY                   * " << endl
		 << " *            DOS REGISTED VERSION 1.5             * " << endl
		 << " *            LICENSED TO - AIDAN AEDY             * " << endl
		 << " *************************************************** " << endl;
}		  

 