from selenium import webdriver
from time import sleep
import math
import pandas as pd

# INPUTS HERE ----------------
username = 'that_guy_pret' # your username 
password = 'PASSWORD' # your password 
page_to_scrape = 'that_guy_pret' # page you want to scrape (# works too Ex. #memes)
scroll_down_pages = 1 # number of scroll downs (bigger the number = more posts loaded )
output_file = 'that_guy_pret' # output file name 
driver_location = r'/Users/preethum/Documents/Python Projects/Insta_Bot/chromedriver' # location of the driver
#-----------------------------
memelinks_arr = []
memelinks_arr_real =[]

driver = webdriver.Chrome(driver_location) #opens the webdriver and logs in to the instagram login page
driver.get('https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher')
sleep(2)
user_name = driver.find_element_by_xpath("//input[@name=\"username\"]") # clicks and inputs the username
user_name.click()
user_name.send_keys(username)
print("set username...")

pass_word = driver.find_element_by_xpath("//input[@name=\"password\"]")# clicks and inputs the password
pass_word.click()
pass_word.send_keys(password)
print("set password...")

login_button = driver.find_element_by_xpath("//button[@type=\"submit\"]") # clicks the login button
login_button.click()
print("We are in baby!...")
sleep(5)

driver.find_element_by_xpath("//button[text()='Not Now']").click() # clicks not now on the webpage
print("clicked not to save login...")

sleep(2)
driver.find_element_by_xpath("//button[text()='Not Now']").click() # clicks another not now on the webpage
print("clicked not to show notifications...")

if page_to_scrape[0] == '#': # checks if the page is a # page or a user page 
    page_to_scrape = page_to_scrape.replace('#','')
    driver.get('https://www.instagram.com/explore/tags/' + page_to_scrape)
else:
    driver.get('https://www.instagram.com/' + page_to_scrape)

print("found the page... ")

for i in range(0,scroll_down_pages): # loops a scrolling down and saves 
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    print("scrolling and grabbing the links...")
    for a in driver.find_elements_by_xpath('.//a'):
        memelinks_arr.append(a.get_attribute('href')) #grabs every link in the page and saves it to memelinks_arr
    sleep(2)
print("finished scrolling down the pages...")

for num in memelinks_arr: # removes duplicate links
    if num not in memelinks_arr_real:
        memelinks_arr_real.append(num) 

exclude = [ # list of links that are not instagram pages
'https://www.instagram.com/legal/privacy/',
'https://www.instagram.com/{}/'.format(username),
'https://www.instagram.com/',
'https://www.instagram.com/direct/inbox/',
'https://www.instagram.com/explore/',
'https://www.instagram.com/accounts/activity/',
'https://about.instagram.com/about-us',
'https://help.instagram.com/',
'https://instagram-press.com/',
'https://www.instagram.com/developer/',
'https://www.instagram.com/about/jobs/',
'https://www.instagram.com/legal/terms/',
'https://www.instagram.com/explore/locations/',
'https://www.instagram.com/directory/hashtags/',
'https://www.instagram.com/{}/followers/'.format(page_to_scrape),
'https://www.instagram.com/{}/following/'.format(page_to_scrape),
'https://www.instagram.com/{}/followers/mutualOnly'.format(page_to_scrape),
'https://www.instagram.com/{}/'.format(page_to_scrape),
'https://www.instagram.com/{}/tagged/'.format(page_to_scrape),
'https://www.instagram.com/software_blogs/',
'https://www.instagram.com/{}/channel/'.format(page_to_scrape),
'https://www.instagram.com/directory/profiles/',
'https://www.instagram.com/explore/tags/{}/'.format(page_to_scrape),
'https://www.instagram.com/work/',
'https://www.instagram.com/clips/',
'https://www.instagram.com/accounts/edit/',
'https://www.instagram.com/{}/saved/'.format(page_to_scrape),
'https://www.instagram.com/phttps://www.instagram.com/directory/suggested/{}'.format(page_to_scrape),
'https://www.instagram.com/directory/suggested/{}'.format(page_to_scrape),
]


memelinks_arr_temp = list(memelinks_arr_real) # creates a copy of the list of posts
current_post_num = 0
memelinks_arr_final = []
for temp in memelinks_arr_temp: # checks if the list contains non post links and removes them 
    if temp in exclude:
        memelinks_arr_real.remove(temp)
        print("{} removed!".format(temp))
    elif 'https://www.instagram.com/explore/tags/' in temp:
        memelinks_arr_real.remove(temp)
        print("{} removed!!".format(temp))
    elif 'https://l.instagram.com/?u=' in temp:
        
        memelinks_arr_real.remove(temp)
        print("{} removed!!".format(temp))
    else:
        memelinks_arr_final.insert( 0,memelinks_arr_real[current_post_num].replace('https://www.instagram.com/p',''))
        current_post_num = current_post_num + 1
        print("Got post #{}...".format(current_post_num))

print("All posts saved")

df = pd.DataFrame()
user_name = []
post_date = []
is_verified = []
photo_vid = []
video_views = []
post_likes = []

data_count = 0
for links in memelinks_arr_final: # loops though every post in the list and pulls data
    driver.get('https://www.instagram.com/p'+ links )

    if len(driver.find_elements_by_xpath("//a[contains(text(),'Go back to Instagram.')]"))!=0: # checks if a link is a removed post
        user_name.append(None)
        post_date.append(None)
        is_verified.append(None)
        photo_vid.append(None)
        video_views.append(None)
        post_likes.append(None)
       
        memelinks_arr_final[data_count] = None
        print("error page")
    else: 
        
        if len(driver.find_elements_by_xpath(".//*[@class='e1e1d']//a"))!=0: # pulling the username 
            user_name.insert(data_count,driver.find_element_by_xpath(".//*[@class='e1e1d']//a").text)
        else:
            user_name.append(None)
        
        if len(driver.find_elements_by_xpath(".//*[@class='_1o9PC Nzb55']"))!=0: # pulling the post date
            post_date.insert(data_count,driver.find_element_by_xpath(".//*[@class='_1o9PC Nzb55']").text)
        else:
            post_date.append(None)

        if len(driver.find_elements_by_xpath(".//*[@class='e1e1d']//span"))!=0: # check if the user is verified
            is_verified.insert(data_count,'True')
        else:
            is_verified.insert(data_count,'False')

        # checks if the post is a video or a photo
        if len(driver.find_elements_by_xpath(".//*[@class='Nm9Fw']//span"))!=0: # photo
            photo_vid.append('Photo')
            video_views.append(None)
            if len(driver.find_elements_by_xpath("(.//*[@type='button']//span)[1]"))!=0: # pulling the post likes
                post_likes.insert(data_count,driver.find_element_by_xpath("(.//*[@type='button']//span)[1]").text)
            else:
                post_likes.append(None)
        else: # video
            photo_vid.append('video')
            
            if len(driver.find_elements_by_xpath(".//*[@class='vcOH2']"))!=0: # pulling the post views
                video_views.insert(data_count,driver.find_element_by_xpath(".//*[@class='vcOH2']//span").text)

                if len(driver.find_elements_by_xpath(".//*[@class='vcOH2']//span")): # pulls the video likes by clicking in the views element
                    driver.find_element_by_xpath(".//*[@class='vcOH2']//span").click()
                else:
                    print('cannot get the video likes')

                if len(driver.find_elements_by_xpath(".//*[@class='vJRqr']//span"))!=0: 
                    post_likes.insert(data_count,driver.find_element_by_xpath(".//*[@class='vJRqr']//span").text)
                else:
                    post_likes.append(None)

            else:
                video_views.append(None)
                post_likes.append(None)
    sleep(1)
    data_count = data_count + 1

    if data_count == 900: # gives the program a cooldown time to combat the instagram cooldown
        print('Cooldown for 3 min...')
        sleep(180)
    elif data_count == 1800:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 2700:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 3600:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 4500:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 5500:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 6500:
        print('Cooldown for 5 min...')
        sleep(300)
    elif data_count == 7500:
        print('Cooldown for 5 min...')
        sleep(300)
    
    print('Getting Post #{}'.format(data_count))
        
user_name.reverse() # puts all the list elements in to a dataframe
df['Post_By'] = user_name   
memelinks_arr_final.reverse()
df['Post_Link'] = memelinks_arr_final
post_date.reverse()
df['Post_Date'] = post_date
is_verified.reverse()
df['is_verified'] = is_verified
photo_vid.reverse()
df['Post_Type'] = photo_vid
video_views.reverse()
df['Video_views'] = video_views
post_likes.reverse()
df['Post_likes'] = post_likes

print(df) # prints the final dataframe

output_file = output_file + '.csv' # add .csv to the user input name of the output file

df.to_csv(output_file) # creates a .csv file and stores it at the location of the program

