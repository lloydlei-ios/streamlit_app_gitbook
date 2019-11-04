# ***gitbook auto build***

| author     |  lloydlei-ios | date | 2019-11-04  |
| ------   |  ------------- |---  |---------  | 
| update log  |  - |-  |-  | 



## git_pull_build.sh 
--- 

```
#!/bin/sh -il

cd /gitlab-your-project-clone-directory/
DATE=`date "+%Y-%m-%d"`
NOW=`date "+%Y-%m-%d %H:%M:%S"`
LOGFILE="/tmp/gitbook_build_mon.log.$DATE"



git_pull_build()
{
    NOW=`date "+%Y-%m-%d %H:%M:%S"`

    echo "$NOW git pull begin... ................."  >> $LOGFILE
    IS_SUCC=`git pull | grep "Already up-to-date."`

    NOW=`date "+%Y-%m-%d %H:%M:%S"`
    echo "$NOW git pull end  ... .................git pull IS_SUCC=$IS_SUCC" >> $LOGFILE

    if [ -z "$IS_SUCC" ]; then
        sleep 2
        NOW=`date "+%Y-%m-%d %H:%M:%S"`

        echo "$NOW git build begin ------------------"  >> $LOGFILE
        gitbook build >> $LOGFILE 2>&1

        NOW=`date "+%Y-%m-%d %H:%M:%S"`
        echo "$NOW git build end   ------------------"  >> $LOGFILE
    else
        echo "$NOW git pull end  ... .................git pull NO update so give up gitbook build ..." >> $LOGFILE
    fi


}

git_pull_build
sleep 20
git_pull_build

```

## crontab exec
--- 

> `*/1 * * * * su - root -c "/bin/sh /git_pull_build_sh_dir/git_pull_build.sh"`
