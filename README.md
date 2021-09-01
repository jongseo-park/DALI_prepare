# ***DALI_prepare***

*[DALI search](http://ekhidna2.biocenter.helsinki.fi/dali/)*

<br/>

The running of the local version of DALI search needs several DB files.

The DB is created from PDB files with the file name of 4 letter code. 

This repository has a script for the preparing of those things.

<br/>

단백질 구조 비교를 위한 DALI search 를 local 에서 작동시키기 위해서는 먼저 데이터베이스를 준비해야 합니다.

데이터베이스는 PDB 파일로부터 만들어지고, 모든 PDB 파일은 4 letter code 로 준비되어 있어야만 합니다.

이 저장소에서는 해당 데이터베이스를 준비하는 것을 도와주는 스크립트를 공유합니다.

사용법은 아래와 같습니다.

(한글 사용법을 아래에 따로 작성해 두었습니다.)

<br/>

- - -

## ***How to use***

### **1. Pull the docker image**

    docker pull jongseopark/dali

<br/>

### **2. Directory setup**

Before run the docker container and this script, 

It is recommended setting of the directory as follows.

    Working_dir/

        dali_prepare.py

        pdb/
            several_pdb_files.pdb
            ...
            ...
        
        dat/
            empty_directory


If you have many PDB files in multiple folders, please prepare as follows.

    Working_dir/

        dali_prepare.py

        pdbs/
            folder1/
                pdb_files.pdb
                ...

            folder2/
                pdb_files.pdb
                ...
            
            ...

        dat/
            empty_directory

You can find the `dali_prepare.py` in this repository, and download it directly or using git clone command.

    git clone https://github.com/jongseo-park/DALI_prepare

<br/>

### **3. Run the docker container from the image with mounting of the working directory**

    docker run 
        -it 
        -v "/path/to/working/directory/:/home/dali/run/" 
        -u dali 
        jongseopark/dali:v01

<br/>

### **4. Run the script**

Run the script with several arguments as follows.



    python3 dali_prepare.py

        --dalipath /opt/DaliLite.v5/
        --pdbpath ./pdb/
        --datpath ./dat/

        --renamer y
        (or --importer y)
        (or --listmaker y)

You have to select only one function at a time (renamer / importer / listmaker).

If you have many PDB files in multiple folders, then use the `pdbspath` and `renamer2` arguments as follows.

    python3 dali_prepare.py

        --dalipath /opt/DaliLite.v5/
        --pdbspath ./pdbs/
        --datpath ./dat/

        --renamer2 y


1. When you run the `renamer` or `renamer2`, the name of your PDB files will be changed to 4 letter codes without overlap, and the log file for replacement (.txt) will be written in the path to PDB.

2. When you run the `importer`, DALI will make the data files (.dat) from your PDB files. For this function, you have to replace the name of your PDB files as 4 letter codes such as `abcd`.

3. When you run the `listmaker`, the script collect the name of data files (.dat) from your `datpath` (./dat/), and write a `dat.list` file comprising all of the name of .dat files in the working directory.
        

<br/>

### **5. Run the DALI**

The docker image already has a local version of DALI (DaliLite.v5) that supports multicore processing (using openmpi).

You can use it as follows (np = the number of processors).

    dali.pl --query ./query.list --db ./dat.list --dat1 /working/dir/query_DAT --dat2 /working/dir/DAT/ --np 10 --TITLE title_you_want --clean

Note that the query.list file has the identical format as the dat.list file.

Please refer to the manual in the hompage of DALI server.

<br/>
<br/>


*Thanks.*

- - -
- - -
<br/>

*For Korean*

<br/>

## ***사용법***

### **1. 도커 이미지 준비하기**

    docker pull jongseopark/dali

<br/>

### **2. 디렉토리 설정**

도커 컨테이너와 스크립트를 사용하기 전에 디렉토리를 세팅하는 것을 추천합니다.

디렉토리는 아래와 같이 구성하면 되겠습니다.

    Working_dir/

        dali_prepare.py

        pdb/
            several_pdb_files.pdb
            ...
            ...
        
        dat/
            empty_directory


만일 많은 PDB 파일을 담고 있는 여러 폴더가 있다면 아래와 같이 준비하세요.


    Working_dir/

        dali_prepare.py

        pdbs/
            folder1/
                pdb_files.pdb
                ...

            folder2/
                pdb_files.pdb
                ...
            
            ...

        dat/
            empty_directory

`dali_prepare.py` 는 이 저장소에서 직접 다운로드 하거나, git clone 명령어를 통해 다운로드할 수 있습니다.

    git clone https://github.com/jongseo-park/DALI_prepare


<br/>

### **3. 도커 이미지를 이용하여 컨테이너 만들고 작업 디렉토리 연결하기**

    docker run 
        -it 
        -v "/path/to/working/directory/:/home/dali/run/" 
        -u dali 
        jongseopark/dali:v01

<br/>

### **4. 스크립트 실행**

아래의 옵션들을 활용하여 스크립트를 실행합니다.



    python3 dali_prepare.py

        --dalipath /opt/DaliLite.v5/
        --pdbpath ./pdb/
        --datpath ./dat/

        --renamer y
        (or --importer y)
        (or --listmaker y)

한 번에 한 가지의 기능만을 사용해야 합니다 (renamer / importer / listmaker).

만일 많은 PDB 파일을 담고 있는 여러 폴더가 있을 때 파일 이름을 변경하고 싶다면 아래와 같이 `pdbspath` 와 `renamer2'*** 옵션을 이용하세요.

    python3 dali_prepare.py

        --dalipath /opt/DaliLite.v5/
        --pdbspath ./pdbs/
        --datpath ./dat/

        --renamer2 y


1. `renamer` 또는 `renamer2` 를 실행시키면, 모든 PDB 파일의 이름이 서로 중복되지 않는 4 letter code 로 변경됩니다. 그리고 이름 변경에 대한 로그파일 (.txt) 이 pdbpath 에 생성됩니다.

2. `importer` 를 실행시키면, DALI 는 PDB 파일을 이용하여 데이터 파일 (.dat) 을 생성합니다. 이 때, PDB 파일의 이름은 모두 `abcd` 와 같은 4 letter code 로 되어있어야만 합니다.

3. `listmaker` 를 실행시키면, 스크립트는 모든 데이터 파일 (.dat) 의 이름을 읽어들인 후 `dat.list` 파일에 옮겨붙입니다. dat.list 파일은 작업 디렉토리 내에 생성됩니다.
        

<br/>

### **5. DALI 실행**

도커 이미지에는 다중 코어 프로세싱 작업이 가능하도록 셋업된 (using openmpi) DALI 의 local version 이 설치되어 있습니다.

아래와 같이 사용할 수 있습니다.

(np = the number of processors).

    dali.pl --query ./query.list --db ./dat.list --dat1 /working/dir/query_DAT --dat2 /working/dir/DAT/ --np 10 --TITLE title_you_want --clean


참고로, query.list 파일은 dat.list 파일과 동일한 형식으로 작성하면 됩니다.

DALI 의 자세한 사용법은 홈페이지를 참조하세요.

<br/>
<br/>


*감사합니다.*