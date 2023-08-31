 # DRUG ANALYSER
    #### Video Demo:  <https://youtu.be/8EB9E9e_-v4>
    #### Description:
    SOURCE
    Drug analyser takes a drug(scientific name) and it returns the indications, function and synonyms
    The code is more complex than it seems. The source is the therapeutic drug database(the largest source
    of information on drugs in the internet). All the .txt and .xls files were converted into csvs and reformatted to include three columns(as in the drugs_to_csv and new_csv functions) in order to decode the information. The csv files should be included in the project directory along with some of the original txt
    files.

    GET INDEX AND GET TARGET FUNCTIONS
    These functions take the input, format it and search the csvs to return the index used in the therapeutic drug database.

    GET INDICATIONS
    With the index available, this functions searches for the drugs uses which are in an illegible format. I chose to format the output in a list with some link works added(add_for) and some commas removed to make it more understandable to the user and to print it out slowly so the user can follow what the program is doing.

    GET FUNCTION and GET SYNONYMS
    These functions use new csvs to get the functions and synonyms of the drugs. These need a yes or no to be outputed, given some users may not need this information. I chose to use a list for the synonyms and print it out line by line via list comprehension over an incoherrent mess if printed out all at once.

    The program says goodbye in a slowly typed goodbye message followed by some terminal art to leave a good impression on the user.

    The link to the TTD database is: https://db.idrblab.net/ttd/full-data-download


