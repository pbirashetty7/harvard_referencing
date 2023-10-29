import streamlit as st

# Dropdown for source type

source_type = st.sidebar.selectbox(
  "Select the type of source you're referencing:", [
    'Books', 'Journals', 'Electronic Sources',
    'Lectures, Tutorials, & Meetings', 'Study Guides & Online Course Material',
    'Social Media', 'Generative AI Tools'
  ])

# For Books
if source_type == 'Books':
  author = st.text_input("Author(s):")
  title = st.text_input("Title of Book:")
  publisher = st.text_input("Publisher:")
  year_of_publication = st.date_input("Year of Publication:",
                                      format="YYYY").year

  edition = st.text_input("Edition (optional):")
  volume = st.text_input("Volume (optional):")

  page_or_range = st.radio(
    'Are you referencing a specific page or a range of pages?',
    ['Specific Page', 'Range of Pages', 'Neither'])

  if page_or_range == 'Specific Page':
    page_number = st.number_input('Enter the specific page number',
                                  min_value=1)
  elif page_or_range == 'Range of Pages':
    start_page = st.number_input('Enter the starting page number', min_value=1)
    end_page = st.number_input('Enter the ending page number',
                               min_value=start_page)

  if not author or not title or not publisher or not year_of_publication:
    st.warning("Please fill in all the required fields.")

# For Journals
elif source_type == 'Journals':
  author = st.text_input("Author(s):")
  article_title = st.text_input("Title of Article:")
  journal_name = st.text_input("Journal Name:")
  year_of_publication = st.text_input("Year of Publication:")
  volume_number = st.text_input("Volume Number:")
  issue_number = st.text_input("Issue Number:")
  page_or_range = st.radio(
    'Are you referencing a specific page or a range of pages?',
    ['Specific Page', 'Range of Pages', 'Neither'])
  if page_or_range == 'Specific Page':
    page_number = st.number_input('Enter the specific page number',
                                  min_value=1)
  elif page_or_range == 'Range of Pages':
    start_page = st.number_input('Enter the starting page number', min_value=1)
    end_page = st.number_input('Enter the ending page number',
                               min_value=start_page)

# For Electronic Sources
elif source_type == 'Electronic Sources':
  author = st.text_input("Author(s):")
  title = st.text_input("Title of Electronic Source:")
  year_of_publication = st.text_input("Year of Publication:")
  url = st.text_input("URL:")
  access_date = st.text_input("Access Date:")

# For Lectures, Tutorials, & Meetings
elif source_type == 'Lectures, Tutorials, & Meetings':
  lecturer = st.text_input("Lecturer/Presenter:")
  title = st.text_input("Title of Lecture/Tutorial/Meeting:")
  date_of_lecture = st.text_input("Date:")

# For Study Guides & Online Course Material
elif source_type == 'Study Guides & Online Course Material':
  author = st.text_input("Author(s)/Organization:")
  title = st.text_input("Title of Material:")
  year_of_publication = st.text_input("Year of Publication:")
  url = st.text_input("URL:")
  access_date = st.text_input("Access Date:")

# For Social Media
elif source_type == 'Social Media':
  username = st.text_input("Username:")
  platform = st.text_input("Platform:")
  date_of_post = st.text_input("Date of Post:")
  url = st.text_input("URL:")

# For Generative AI Tools
elif source_type == 'Generative AI Tools':
  tool_name = st.text_input("Name of the Tool:")
  version = st.text_input("Version (if applicable):")
  date_of_access = st.text_input("Date of Access:")
  url = st.text_input("URL:")

# Sidebar Help/Tutorial Content

st.header('Citation Help & Guidelines')
st.write(f'You selected: **{source_type}**')

# Guidelines for Books
if source_type == 'Books':
  st.write("#### Books:")
  st.write(
    "To cite a book, you'll need the author name, title, publisher, and publication year. If available, also provide the edition and volume."
  )

# Guidelines for Journals
elif source_type == 'Journals':
  st.write("#### Journals:")
  st.write(
    "For journal articles, provide the article author, article title, journal name, publication year, volume, issue, and page numbers."
  )

# Guidelines for Electronic Sources
elif source_type == 'Electronic Sources':
  st.write("#### Electronic Sources:")
  st.write(
    "For websites and electronic sources, mention the website name, page title, and URL. Don't forget the date you accessed the content."
  )

# Guidelines for Lectures, Tutorials, & Meetings
elif source_type == 'Lectures, Tutorials, & Meetings':
  st.write("#### Lectures, Tutorials, & Meetings:")
  st.write(
    "Citing lectures, tutorials, or meetings requires the lecturer or presenter's name, the title, the institution, and the date it was presented."
  )

# Guidelines for Study Guides & Online Course Material
elif source_type == 'Study Guides & Online Course Material':
  st.write("#### Study Guides & Online Course Material:")
  st.write(
    "For study guides and online course materials, state the course name, course code, institution, and the date accessed."
  )

# Guidelines for Social Media
elif source_type == 'Social Media':
  st.write("#### Social Media:")
  st.write(
    "Citing social media posts requires the platform name, post author or username, post title or first few words, date posted, and the URL."
  )

# Guidelines for Generative AI Tools
elif source_type == 'Generative AI Tools':
  st.write("#### Generative AI Tools:")
  st.write(
    "When citing generative AI tools, provide the tool's name, provider, and the date you used it."
  )

# Backend Citation Generator


def book_citation(author,
                  title,
                  publisher,
                  year_of_publication,
                  edition=None,
                  volume=None,
                  page_or_range=None):
  citation = f"{author}. ({year_of_publication}). {title}. {publisher}."
  if volume:
    citation += f" Vol. {volume}."
  if edition:
    citation += f" {edition} edition."
  if page_or_range:
    if isinstance(page_or_range, int):  # Single page
      citation += f" p. {page_or_range}."
    elif isinstance(page_or_range, tuple):  # Page range
      citation += f" pp. {page_or_range[0]}-{page_or_range[1]}."
  return citation


def journal_citation(author,
                     article_title,
                     journal_name,
                     year_of_publication,
                     volume_number="",
                     issue_number="",
                     page_or_range=None):
  citation = f"{author} ({year_of_publication}). <i>{article_title}</i>. {journal_name}"
  if volume_number and issue_number:
    citation += f", {volume_number}({issue_number})"
    if page_or_range:
      if isinstance(page_or_range, int):  # Single page
        citation += f" p. {page_or_range}."
      elif isinstance(page_or_range, tuple):  # Page range
        citation += f" pp. {page_or_range[0]}-{page_or_range[1]}."
  return citation  # Moved this line to be outside the nested conditional


def electronic_source_citation(author,
                               title,
                               year_of_publication,
                               url,
                               access_date=""):
  citation = f"{author} ({year_of_publication}). <i>{title}</i>. Retrieved from {url}"
  if access_date:
    citation += f" on {access_date}."
  else:
    citation += "."
  return citation


def lecture_citation(lecturer, title, date_of_lecture):
  return f"{lecturer} ({date_of_lecture}). <i>{title}</i>. Lecture."


def study_guide_citation(author,
                         title,
                         year_of_publication,
                         url,
                         access_date=""):
  citation = f"{author} ({year_of_publication}). <i>{title}</i>. Retrieved from {url}"
  if access_date:
    citation += f" on {access_date}."
  else:
    citation += "."
  return citation


def social_media_citation(username, platform, date_of_post, url):
  return f"{username} ({date_of_post}). [Status update]. {platform}. Retrieved from {url}."


def ai_tool_citation(tool_name, version="", date_of_access="", url=""):
  citation = f"{tool_name}"
  if version:
    citation += f" (Version {version})"
  citation += " [Software]."
  if date_of_access and url:
    citation += f" Retrieved {date_of_access}, from {url}."
  elif url:
    citation += f" Retrieved from {url}."
  return citation


# Using the above functions based on the user's source type selection

if source_type == 'Books':
  if page_or_range == 'Specific Page':
    citation_result = book_citation(author, title, publisher,
                                    year_of_publication, edition, volume,
                                    page_number)
  elif page_or_range == 'Range of Pages':
    citation_result = book_citation(author, title, publisher,
                                    year_of_publication, edition, volume,
                                    (start_page, end_page))
  else:
    citation_result = book_citation(author, title, publisher,
                                    year_of_publication, edition, volume)

elif source_type == 'Journals':
  if page_or_range == 'Specific Page':
    citation_result = journal_citation(author, article_title, journal_name,
                                       year_of_publication, volume_number,
                                       issue_number, page_number)
  elif page_or_range == 'Range of Pages':
    citation_result = journal_citation(author, article_title, journal_name,
                                       year_of_publication, volume_number,
                                       issue_number, (start_page, end_page))
  else:
    citation_result = journal_citation(author, article_title, journal_name,
                                       year_of_publication, volume_number,
                                       issue_number)

elif source_type == 'Electronic Sources':
  citation_result = electronic_source_citation(author, title,
                                               year_of_publication, url,
                                               access_date)
  citation_result = electronic_source_citation(author, title,
                                               year_of_publication, url,
                                               access_date)

elif source_type == 'Lectures, Tutorials, & Meetings':
  citation_result = lecture_citation(lecturer, title, date_of_lecture)

elif source_type == 'Study Guides & Online Course Material':
  citation_result = study_guide_citation(author, title, year_of_publication,
                                         url, access_date)

elif source_type == 'Social Media':
  citation_result = social_media_citation(username, platform, date_of_post,
                                          url)

elif source_type == 'Generative AI Tools':
  citation_result = ai_tool_citation(tool_name, version, date_of_access, url)

# Backend In-Text Citation Generator


def book_in_text_citation(author, year_of_publication):
  return f"({author}, {year_of_publication})"


def journal_in_text_citation(author, year_of_publication):
  return f"({author}, {year_of_publication})"


def electronic_source_in_text_citation(author, year_of_publication):
  return f"({author}, {year_of_publication})"


def lecture_in_text_citation(lecturer, date_of_lecture):
  return f"({lecturer}, {date_of_lecture.split('-')[0]})"  # Assuming date format is YYYY-MM-DD


def study_guide_in_text_citation(author, year_of_publication):
  return f"({author}, {year_of_publication})"


def social_media_in_text_citation(username, date_of_post):
  return f"({username}, {date_of_post.split('-')[0]})"  # Assuming date format is YYYY-MM-DD


def ai_tool_in_text_citation(tool_name):
  return f"({tool_name})"


# Using the above in-text functions based on the user's source type selection

if source_type == 'Books':
  in_text_result = book_in_text_citation(author, year_of_publication)

elif source_type == 'Journals':
  in_text_result = journal_in_text_citation(author, year_of_publication)

elif source_type == 'Electronic Sources':
  in_text_result = electronic_source_in_text_citation(author,
                                                      year_of_publication)

elif source_type == 'Lectures, Tutorials, & Meetings':
  in_text_result = lecture_in_text_citation(lecturer, date_of_lecture)

elif source_type == 'Study Guides & Online Course Material':
  in_text_result = study_guide_in_text_citation(author, year_of_publication)

elif source_type == 'Social Media':
  in_text_result = social_media_in_text_citation(username, date_of_post)

elif source_type == 'Generative AI Tools':
  in_text_result = ai_tool_in_text_citation(tool_name)

# Display both in-text citation and reference list citation

st.markdown("In-text citation:\n" + in_text_result, unsafe_allow_html=True)
st.markdown("In reference list:\n" + citation_result, unsafe_allow_html=True)
