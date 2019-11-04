# ***gitbook integrate config***

| author     |  lloydlei-ios | date | 2019-11-04  |
| ------   |  ------------- |---  |---------  | 
| update log  |  - |-  |-  | 

## gitbook nginx config
--- 
- Nginx reverse proxy gitbook directory named _book 


```
location ^~ /gitlab-your-project-name {
    alias        /gitlab-your-project-clone-directory/_book/;
    index        index.html;
    auth_basic   "gitbook gitlab-your-project-name";
    auth_basic_user_file /auth_basic_pwd_dir/auth_basic_pwd;
}

```
