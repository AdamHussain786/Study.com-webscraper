#Copyright Adam. Don't be stealing my stuff man!

from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import csv
from filename_sanitizer import sanitize_path_fragment

links =["https://study.com/academy/lesson/books-about-south-african-history-politics.html",
"https://study.com/academy/lesson/alan-paton-biography-books-quotes.html",
"https://study.com/academy/lesson/alan-patons-writing-style-for-cry-the-beloved-country.html",
"https://study.com/academy/lesson/why-did-alan-paton-write-cry-the-beloved-country.html",
"https://study.com/academy/lesson/why-is-cry-the-beloved-country-a-great-work-of-literature.html",
"https://study.com/academy/lesson/historical-significance-of-cry-the-beloved-country.html",
"https://study.com/academy/lesson/cry-the-beloved-country-significance-of-the-title.html",
"https://study.com/academy/lesson/cry-the-beloved-country-plot-overview-major-events.html",
"https://study.com/academy/lesson/setting-of-cry-the-beloved-country-ndotsheni-johannesburg.html",
"https://study.com/academy/lesson/shantytowns-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/shantytowns-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/tribal-systems-broken-tribes-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/literary-criticism-of-cry-the-beloved-country.html",
"https://study.com/academy/lesson/conflict-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/gender-roles-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/social-class-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/theme-of-pain-suffering-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/theme-of-religion-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/themes-of-race-racism-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/themes-of-race-racism-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/paradoxes-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/redemption-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/social-issues-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/theme-of-fear-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/symbols-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/land-symbolism-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/historical-allusions-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/biblical-allusions-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/motifs-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/christian-motifs-religious-imagery-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/examples-of-imagery-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/examples-of-dramatic-irony-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/examples-of-verbal-irony-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/similes-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/repeated-phrases-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/point-of-view-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/reverend-stephen-kumalo-in-cry-the-beloved-country-character-analysis.html",
"https://study.com/academy/lesson/james-jarvis-in-cry-the-beloved-country-character-analysis.html",
"https://study.com/academy/lesson/james-jarvis-stephen-kumalo-relationship-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/similarities-differences-of-james-jarvis-stephen-kumalo.html",
"https://study.com/academy/lesson/theophilus-msimangu-in-cry-the-beloved-country-character-quotes.html",
"https://study.com/academy/lesson/absalom-kumalo-in-cry-the-beloved-country-character-traits-analysis-death.html",
"https://study.com/academy/lesson/stephen-kumalo-absalom-kumalo-relationship-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/john-kumalo-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/comparing-stephen-kumalo-john-kumalo-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/arthur-jarvis-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/father-vincent-in-cry-the-beloved-country.html",
"https://study.com/academy/topic/cry-the-beloved-country-major-characters.html",
"https://study.com/academy/lesson/gertrude-from-cry-the-beloved-country-analysis-quotes.html",
"https://study.com/academy/lesson/mrs-lithebe-in-cry-the-beloved-country-character-quotes.html",
"https://study.com/academy/lesson/absaloms-girlfriend-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/matthew-kumalo-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/mr-carmichael-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/dubula-tomlinson-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/john-harrison-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/mr-mrs-harrison-in-cry-the-beloved-country.html",
"https://study.com/academy/topic/cry-the-beloved-country-minor-characters.html",
"https://study.com/academy/lesson/stephen-kumalo-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/john-kumalo-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/absalom-kumalo-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/arthur-jarvis-in-cry-the-beloved-country-quotes-speech-last-words.html",
"https://study.com/academy/lesson/james-jarvis-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/father-vincent-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/mr-carmichael-quotes-from-cry-the-beloved-country.html",
"https://study.com/academy/lesson/social-injustice-in-cry-the-beloved-country-quotes-examples.html",
"https://study.com/academy/lesson/quotes-about-racism-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/apartheid-in-cry-the-beloved-country-quotes-examples.html",
"https://study.com/academy/lesson/quotes-about-religion-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-fear-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-hope-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-family-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-father-son-relationships-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-johannesburg-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-johannesburg-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/quotes-about-the-land-in-cry-the-beloved-country.html",
"https://study.com/academy/topic/cry-the-beloved-country-quotations.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-1-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-2-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-3-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-4-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-5-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-6-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-7-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-8-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-9-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-10-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-11-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-12-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-13-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-14-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-15-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-16-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-17-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-18-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-19-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-20-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-21-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-22-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-23-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-24-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-25-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-26-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-27-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-28-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-29-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-30-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-31-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-32-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-33-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-34-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-35-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-chapter-36-summary.html",
"https://study.com/academy/lesson/cry-the-beloved-country-unit-plan.html",
"https://study.com/academy/lesson/cry-the-beloved-country-lesson-plan.html",
"https://study.com/academy/lesson/cry-the-beloved-country-discussion-questions.html",
"https://study.com/academy/lesson/cry-the-beloved-country-questions-by-chapter.html",
"https://study.com/academy/lesson/questions-about-absalom-kumalo-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/questions-about-james-jarvis-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/questions-about-arthur-jarvis-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/questions-about-father-vincent-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/questions-about-father-vincent-in-cry-the-beloved-country.html",
"https://study.com/academy/lesson/cry-the-beloved-country-essay-topics-writing-prompts.html",
"https://study.com/academy/lesson/cry-the-beloved-country-activities.html",
"https://study.com/academy/topic/teaching-cry-the-beloved-country.html"


]

 #Insert any study.com link
    #Establishing soup

  #Find the correct/relevant div



for link in links:
    r = requests.get(link)  
    soup = BeautifulSoup(r.content, features="lxml")
    articles = soup.find_all('div', id='articleMain')
    title = soup.find('h1')

    unsanitized_filename = title.text.replace(" ", "")
    sanitized_filename = sanitize_path_fragment(unsanitized_filename,

    target_file_systems = {'ntfs_win32'}, replacement = u'-')

    print (sanitized_filename)

    file_name = sanitized_filename + '.csv'
    print(file_name)
    csv_file = open(file_name, 'w')
    csv_writer = csv.writer(csv_file)                   #CSV code to open and setup excel file
    csv_writer.writerow(['title', 'header', 'summary']) 

    for article in articles:                    #For every article there is in the article div
        for header in article.find_all('h2'):   #For all the headers found
            
            print(header.text)  #Print the header text for debugging

            nextNode = header
            while True:
                nextNode = nextNode.nextSibling
                if nextNode is None:
                    break
                if isinstance(nextNode, NavigableString):
                    print (nextNode.strip())                        #This code essentially checks all the information between two headers
                if isinstance(nextNode, Tag):
                    if nextNode.name == "h2":
                        break
                    paragraph_text = nextNode.get_text(strip=True).strip()
                    print (paragraph_text)
            print('\n')     #Blank line

            csv_writer.writerow([title.text ,header.text, paragraph_text])      #Write the info to the excel file 


csv_file.close()    #Close the csv after we done wid it