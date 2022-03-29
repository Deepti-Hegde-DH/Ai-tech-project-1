# Python programming project-1
PROBLEM STATEMENT- 
You need to develop a programming solution in the form of python script(s) to solve the business problem given in the following case.
You are assigned by Mr. Smith, head of IT support at your Business School, to develop a room- booking system similar to the one used by the central university
1. Viewthedetailofanyspecifiedroom(e.g.2.005),suchascapacity, equipment, location, availability, etc., and then book the room if available.
2. Searchavailableroombasedongivencriteria,suchastime slots(required), capacity (optional), and equipment (optional).
For demonstration, you may generate an arbitrary dataset based on rooms listed in the central university system. An example data set is shown in the appendix. Your dataset can be structured differently.

SOLUTION
The solution is coded and is available in the repository. Solotion uses Tkinter and Pandas library. main window handels problem statement 1 and problem statement 2 seperately. the dataset compatible is a csv /excel file.



FUNCTION Definitions and global VARIABLE description.

rootW - the main/opening widow that contains the  options  
		statement 1-to choose a room and view its details(room 		name ,equipment, capacity).
		statement 2-to search for a specific room with given criteria (date 		(required), slot (required),capacity(optional),equipment(optional)

Selectroom- the menu  on the main window(rootW) that  enables the 			   user to choose room for statement 1
	the choice is executed using “go” button

Selectroom0- the menu on rootW that enables user to choose time slot			for search  (statement 2)

Selectroom1- the menu on rootW that enables user to choose  capacity			for search  (statement 2)

Selectroom2- the menu on rootW that enables user to choose  				equipment	 for search  (statement 2)

Cal- calendar to choose the date , present on  rootW  

Def crtW1()-  creates a window W1 that pops up when go is clicked.it 				displays the  details of room chosen wrt to selectroom
				also contains button “book room”
    				when book room is clicked, W1 window is destroyed and
				crtW3() is invoked

Def crtW3()- creates a new window W3 that accepts room booking 			   details and contains cal ( to choose booking date),
			   menu bar selectroom (to choose time slot ),
			   confirm button (pops up confirmation message and returns 			  to main screen rootW) invoking def confirm()(destroys W3)
Def  gdt()- to extract date from calendar

Def crtW2()-creates a new window to show search results based on 			  available criteria chosen from 				selectroom0,selectroom1,selectroom2









