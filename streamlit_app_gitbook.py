# coding: utf-8
import streamlit as st
import sys   
reload(sys) 
sys.setdefaultencoding('utf-8')


__CONST_RE_DEF_DIR_GITBOOK_PAGE=r'\[(.*)\]\((.*)\)'
__CONST_STR_DEF_SUMMARY_MD_FILE_PATH = './SUMMARY.md'
__CONST_STR_DEF_MAIN_PAGE_INDEX_TITLE = "Streamlit gitbook App"
__CONST_STR_DEF_MAIN_PAGE_UNKNOWN = 'Unknown page'
__CONST_STR_DEF_SIDEBAR_TITLE = 'Gitbook summary'
__CONST_STR_DEF_MAIN_PAGE_HEADER_LINE = "--- "
__CONST_STR_DEF_SIDEBAR_SEARCH_ELEMENT = "Search page"
__CONST_STR_DEF_SIDEBAR_CHOOSE_ELEMENT = "Choose page"
__CONST_STR_DEF_ERROR_MD_DIR  = "Gitbook directory , please select a subdirectory"


def make_gitbook_page(line) :
    import re
    dir_page = (__CONST_STR_DEF_MAIN_PAGE_UNKNOWN,'')
    dir_page_ret = re.findall(__CONST_RE_DEF_DIR_GITBOOK_PAGE,line)
    if dir_page_ret :
        dir_page = [dir_page_ret[0][0],dir_page_ret[0][1]]
    else:
        print "summary line[{}] was not match pattern".format(line)
        dir_page = None
    return dir_page

def write_gitbooke_page(md_page) :  
     import os
     parent_path =  os.path.abspath('..')
     with open(u"./"+md_page,'r',1024) as f :
        lines = f.read()
        st.markdown(lines,unsafe_allow_html=True)

def search_page(md_pages={},sreach_str="") :
    s_ret =  dict((key, value) for key, value in md_pages.items() if str(key).find(sreach_str) >= 0)
    return s_ret

st.title(__CONST_STR_DEF_MAIN_PAGE_INDEX_TITLE)

md_pages = {}
st.sidebar.title(__CONST_STR_DEF_SIDEBAR_TITLE)
with open(__CONST_STR_DEF_SUMMARY_MD_FILE_PATH,'r',1024) as f_sum :
    line = f_sum.readline()
    while line :
        line = line.strip()
        if len(line) > 0 :
            gpg = make_gitbook_page(line)
            if  gpg:
                md_pages[gpg[0]] = gpg[1]
        line = f_sum.readline()

search_page_str = st.sidebar.text_input(__CONST_STR_DEF_SIDEBAR_SEARCH_ELEMENT)
print u"search --> value=" + search_page_str
search_ret  = {}
if search_page_str :
    search_ret = search_page(md_pages,search_page_str)
    md_pages = search_ret

selection = st.sidebar.radio(__CONST_STR_DEF_SIDEBAR_CHOOSE_ELEMENT, list(sorted(md_pages.keys())))
print u"select --> value=" + md_pages[selection]

md_page=md_pages[selection]
if md_page :
    st.markdown(__CONST_STR_DEF_MAIN_PAGE_HEADER_LINE)
    st.write("### "+ md_page )
    write_gitbooke_page(md_page)
else:
    st.markdown(__CONST_STR_DEF_MAIN_PAGE_HEADER_LINE)
    st.write(__CONST_STR_DEF_ERROR_MD_DIR)


