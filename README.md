#BookShare
This is a book sharing web app built on Django framework. It uses Google login to log into the app. Every user is given his own profile where he can put the list of books he has and, request for books he wants. To read the motto and vision behind this app please read BuisnessModel.md

###Instructions to run the application
  1. Install all the packages in requirements.txt
  2. Choose this directory and run python manage.py runserver
  3. Go to the following url wizsid11.com:8000/book_share/login
  4. Login with your Gmail id ( Don't try to log in through facebook, as the feature is not implemented)
  5. Fill in your personal details
  
###How to use the application to share books with the community

  1. Add books that you have in the First section by filling in the book name and the author name and clicking the submit button
  2. Click the search button to search for a book, search using the name of the book. If found click on send request to send a request to the owner of the book.
  3. Click on Requests to respond to others requests for your books. You can either accept or delete a request. On accepting your information is shown in the notifications tab of the person who requested for the book. 
  4. Once you get your book back let us know by 'freeing' it using the free tab
  5. Check your notifications in your notification tab to check the responses of your requests
  
  Note: Only accept requests is implemented. Delete can be easily implemented in a similar way to free.
