# Instagram-Scraper
A Instagram Scraper that pulls data from a user or a hashtag page

# Instagram Scraper

### A script that will scrape a users data

## Outputs:
1. Username
2. Date posted
3. Is the person Verified?
4. Is it a Photo or a Video
5. Video views
6. Post likes

## Inputs:
1. username of your own Instagram account 
2. password of your own Instagram account 
3. page to scrape (This can be a user or a # page, if the user is private make sure that your account that you are inputting above follows the account you want to scrape)
4. Pages to scroll (The number of times the program will scroll down to load all the posts from the user. Bigger the number, the program will scrape more posts)
5. Output File name (Outputs outputs to a .csv file)
6. Driver Location (Location of the driver, more on that later)

## How it works:
This program has 5 simple steps:
1. Program opens a new window and directs to the Instagram Login Page
2. Goes to the desired user/# page and starts scrolling down to load all the links to the posts
3. Once the links are saved the program keeps the links that only link to a user post
4. A loop starts where each post will be loaded and scraped 
5. The scraped data will be stored in a data frame and the program will automatically output the .csv file at the location of the .py file

## Output .csv files
    Post_By                                  Post_Link          Post_Date is_verified Post_Type Video_views Post_likes
    0  that_guy_pret  /B3nlGGaAu3qfL7eLnk0fWUkrVJnzR_YG0zpJ1Q0/   OCTOBER 14, 2019       False     Photo        None        234
    1  that_guy_pret  /ByWNWaegcX-x-btsE2o7L8VT_MLBZypgxSz_FQ0/       JUNE 5, 2019       False     Photo        None        228
    2  that_guy_pret  /BsRHtaNnuN-HpPTP680MbbXqhRS8guZPgY8tRY0/    JANUARY 5, 2019       False     Photo        None        198
    3  that_guy_pret  /Br4RDqEnRvEA7JNsGu3kWqGNRZ9LiWflkhJ0Fs0/  DECEMBER 26, 2018       False     Photo        None        184
    4  that_guy_pret  /Bql2kJdnUDj6n0dPkKrfPvBmqGsrDpzAPaqCq40/  NOVEMBER 24, 2018       False     Photo        None        191
    5  that_guy_pret  /BkGQga3nsnN5wN3QKZhkzzm7iGWZUbv6U8Juzs0/      JUNE 16, 2018       False     Photo        None        257
    6  that_guy_pret  /BiXoxHKnqGmm1qHPZdLzhF5iFcNlp9gd4L3twY0/        MAY 4, 2018       False     Photo        None        217
    7  that_guy_pret  /BazT-ZpD51ujqf7XMr7LUYQhei6_L0mvaqIFU00/   OCTOBER 28, 2017       False     Photo        None        242

## Console Logs
    set username...
    set password...
    We are in baby!...
    clicked not to save login...
    clicked not to show notifications...
    found the page... 
    scrolling and grabbing the links...
    finished scrolling down the pages...
    https://www.instagram.com/that_guy_pret/followers/ removed!
    https://www.instagram.com/that_guy_pret/following/ removed!
    https://www.instagram.com/that_guy_pret/ removed!
    https://www.instagram.com/that_guy_pret/tagged/ removed!
    Got post #1...
    Got post #2...
    Got post #3...
    Got post #4...
    Got post #5...
    Got post #6...
    Got post #7...
    Got post #8...
    https://www.instagram.com/ removed!
    https://www.instagram.com/direct/inbox/ removed!
    https://www.instagram.com/explore/ removed!
    https://www.instagram.com/accounts/activity/ removed!
    https://www.instagram.com/seg_fault_11_memes/ removed!
    https://about.instagram.com/about-us removed!
    https://help.instagram.com/ removed!
    https://instagram-press.com/ removed!
    https://www.instagram.com/developer/ removed!
    https://www.instagram.com/about/jobs/ removed!
    https://www.instagram.com/legal/privacy/ removed!
    https://www.instagram.com/legal/terms/ removed!
    https://www.instagram.com/explore/locations/ removed!
    https://www.instagram.com/directory/profiles/ removed!
    https://www.instagram.com/directory/hashtags/ removed!
    All posts saved
    Getting Post #1
    Getting Post #2
    Getting Post #3
    Getting Post #4
    Getting Post #5
    Getting Post #6
    Getting Post #7
    Getting Post #8
            Post_By                                  Post_Link          Post_Date is_verified Post_Type Video_views Post_likes
    0  that_guy_pret  /B3nlGGaAu3qfL7eLnk0fWUkrVJnzR_YG0zpJ1Q0/   OCTOBER 14, 2019       False     Photo        None        234
    1  that_guy_pret  /ByWNWaegcX-x-btsE2o7L8VT_MLBZypgxSz_FQ0/       JUNE 5, 2019       False     Photo        None        228
    2  that_guy_pret  /BsRHtaNnuN-HpPTP680MbbXqhRS8guZPgY8tRY0/    JANUARY 5, 2019       False     Photo        None        198
    3  that_guy_pret  /Br4RDqEnRvEA7JNsGu3kWqGNRZ9LiWflkhJ0Fs0/  DECEMBER 26, 2018       False     Photo        None        184
    4  that_guy_pret  /Bql2kJdnUDj6n0dPkKrfPvBmqGsrDpzAPaqCq40/  NOVEMBER 24, 2018       False     Photo        None        191
    5  that_guy_pret  /BkGQga3nsnN5wN3QKZhkzzm7iGWZUbv6U8Juzs0/      JUNE 16, 2018       False     Photo        None        257

This is a example file, there are some more examples in the project folder, I would also appreciate a follow too :) @that_guy_pret 

## How to install the required elements:
1. pip install selenium, time, math and pandas
2. Get your choice of driver (mine is Chrome and I have the specific diver, make sure its the correct version with the browser you currently have)

## How to run the program:
1. Open the file in your IDE
2. Set the correct parameters at the top of the .py file
3. Make sure that you input the path of your webdriver

## Things to watch out for:
When scraping large files, instagram will give a cool down, this is unpredictable. If this comes up, the program will set all the outputs to None.
Example inputs are shown in the project file!

## Module Versions (may add a virtual environment soon)
1. selenium - 3.141.0
2. time - Any
3. math - Any
4. pandas - 0.24.2

