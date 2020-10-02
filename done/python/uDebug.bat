@echo OFF
@setlocal EnableDelayedExpansion 

cls
echo.
echo ###########################################################
echo #      ** Bat p/ Facilitar o uso do uDebug no URI **      #
echo #       ** Use p/ programas em C, C++ ou Python **        #
echo # 00) Este arquivo deve estar na pasta "Debug" do projeto #
echo # 01) Acesse "www.udebug.com/URI/", no problema desejado  #
echo # 02) Selecione algum Input, clicando nele                #
echo # 03) Copie o conteudo do Input (Copy Input)              #
echo # 04) Abra o bloco de notas                               #
echo # 05) Cole o conteudo dentro do bloco de notas (ctrl+v)   #
echo # 06) No bloco de notas, clique em arquivo -^> salvar como #
echo # 07) Econtre a pasta do projeto criado pelo Code:Blocks, #
echo #     dentro dela deve haver uma pasta "bin",             #
echo #     e dentro dela uma pasta "Debug".                    #
echo # 08) Save o arquvio dentro da pasta "Debug" do projeto.  # 
echo # 09) Sugiro salvar este arquivo com o nome: Input.txt    # 
echo # 10) Depois digite enter p/ executar este script         #
echo # ------------------------------------------------------- #
echo #                                                         #
echo #               -= Elder Sobrinho (UFTM) =-               #
echo #                    Copyright - 2020                     #
echo #                                                         #
echo ###########################################################
echo.
pause

set EXE=.exe
set PY=.py
set TXT=.txt

set UsePython=0
choice /C YN /M "Seu codigo foi escrito em Python? Y - Yes, N - Not"
IF ERRORLEVEL 2 ( goto GetFile )

set "Conda=0"
set UsePython=1
set PythonP=python.exe

rem SET PATH=%PATH%;%userprofile%\Anaconda3\
if exist "%userprofile%\Anaconda3\Scripts\activate.bat" ( 
	set "Conda=1"
) else (
	where python.exe >nul 2>&1
	IF ERRORLEVEL 1 (
		echo "*****************************************************************"
		echo "Nao encontramos python.exe no computador. Favor Add ele ao path."
		echo "****************************************************************"
		TIMEOUT /T 10  /NOBREAK >nul 2>&1
		GOTO errorHandling
	)
	FOR /F "delims=" %%A IN ('where python.exe') DO (
		%%A -c "print('example'); exit(0)" >nul 2>&1
		rem echo %%A %ERRORLEVEL%
		IF ERRORLEVEL 1 ( 
			echo Error on %%A
		) else (
			set PythonP=%%A
			break
		)
	)
	IF ERRORLEVEL 1 (
		echo "*****************************************************************"
		echo "Nao encontramos uma instalacao funcional do python.exe."
		echo "****************************************************************"
		TIMEOUT /T 10  /NOBREAK >nul 2>&1
		GOTO errorHandling
	)
)
rem echo %PythonP%



:GetFilePy
set /P ExecFile=Informe o nome do arquivo .py: 
if "%ExecFile%"=="" (
	echo Vc nao informou o nome do arquivo .py.
	goto GetFilePy
)
if exist "%ExecFile%%PY%" (
	set "ExecFile=%ExecFile%%PY%"
	goto ExecFileOK
)
if exist "%ExecFile%" (
	if "%ExecFile:~-3%" neq "%PY%" goto  GetFilePy
	goto ExecFileOK
)
echo Arquivo "%ExecFile%" nao encontrado ("%PY%").
goto GetFilePy



:GetFile
set /P ExecFile=Informe o nome do executavel (nome do projeto): 
if "%ExecFile%"=="" (
	echo Vc nao informou o nome do executavel.
	goto GetFile
)
if exist "%ExecFile%%EXE%" (
	set "ExecFile=%ExecFile%%EXE%"
	goto ExecFileOK
)
if exist "%ExecFile%" (
	if "%ExecFile:~-4%" neq "%EXE%" goto  GetFile
	goto ExecFileOK
)
echo Arquivo "%ExecFile%" nao encontrado (executavel).
goto GetFile



:ExecFileOK
:GetInput
set /P InputFile=Informe o nome do arquivo de Input: 
rem if "%InputFile%"=="" goto GetInput
if "%InputFile%"=="" (
	echo Usando nome de arquivo padrao "Input.txt"
	set "InputFile=Input.txt"
)
if exist "%InputFile%%TXT%" (
	set "InputFile=%InputFile%%TXT%"
	goto InputFileOK
)
if "%InputFile%"=="%ExecFile%" (
	echo Arquivo nao pode ter o nome "%ExecFile%".
	goto GetInput
)
if exist "%InputFile%" goto InputFileOK
echo Arquivo "%InputFile%" nao encontrado (Input).
goto GetInput



:InputFileOK
:GetOutput
set /P OutputFile=Informe o nome do arquivo de Output (opcional): 
if "%OutputFile%"=="" (
	echo Usando nome de arquivo padrao "Output.txt"
	set "OutputFile=Output.txt"
	goto Exit
)
if "%OutputFile:~-4%" neq "%TXT%" (
	echo Informe o nome do arquivo de Output no formato: 
	echo     XXXXX.TXT    onde XXXXX e o nome do arquivo
	goto GetOutput
)
goto Exit




:Exit
echo Gerando saida.
set "RunBat=Run.bat"
set "TimeElapsed=TimeElapsed.txt"
if exist "%OutputFile%" del %OutputFile%

echo ^@echo off > %RunBat%
echo ^@setlocal >> %RunBat%


if "%UsePython%"=="1" (
	if "%Conda%"=="1" (
		echo call %%userprofile%%\Anaconda3\Scripts\activate.bat  >> %RunBat%
	)
)

echo set start=%%time%% >> %RunBat%
echo ^@echo on >> %RunBat%

if "%UsePython%"=="1" (
	if "%Conda%"=="1" (
		rem echo call type %InputFile% ^| %PythonP% %ExecFile% ^> %OutputFile% >> %RunBat%
		echo type %InputFile% ^| %PythonP% %ExecFile% ^> %OutputFile% >> %RunBat%
	) else (
		echo type %InputFile% ^| %PythonP% %ExecFile% ^> %OutputFile% >> %RunBat%
	)
) else (
	echo type %InputFile% ^| %ExecFile% ^> %OutputFile% >> %RunBat%
)
echo ^@echo off >> %RunBat%
echo IF %%ERRORLEVEL%% NEQ 0 ( echo ERROR ON RUN ^>^> %OutputFile% >> %RunBat% )

echo set end=%%time%% >> %RunBat%
echo set options=^"tokens=1-4 delims=:.,^" >> %RunBat%
echo for ^/f %%options%% %%%%a in (^"%%start%%^") do set start_h=%%%%a^&set ^/a start_m=100%%%%b %%%% 100^&set ^/a start_s=100%%%%c %%%% 100^&set ^/a start_ms=100%%%%d %%%% 100 >> %RunBat%
echo for ^/f %%options%% %%%%a in (^"%%end%%^") do set end_h=%%%%a^&set ^/a end_m=100%%%%b %%%% 100^&set ^/a end_s=100%%%%c %%%% 100^&set ^/a end_ms=100%%%%d %%%% 100 >> %RunBat%
echo set ^/a hours=%%end_h%%-%%start_h%% >> %RunBat%
echo set ^/a mins=%%end_m%%-%%start_m%% >> %RunBat%
echo set ^/a secs=%%end_s%%-%%start_s%% >> %RunBat%
echo set ^/a ms=%%end_ms%%-%%start_ms%% >> %RunBat%
echo if %%ms%% lss 0 set ^/a secs = %%secs%% - 1 ^& set ^/a ms = 100%%ms%% >> %RunBat%
echo if %%secs%% lss 0 set ^/a mins = %%mins%% - 1 ^& set ^/a secs = 60%%secs%% >> %RunBat%
echo if %%mins%% lss 0 set ^/a hours = %%hours%% - 1 ^& set ^/a mins = 60%%mins%% >> %RunBat%
echo if %%hours%% lss 0 set ^/a hours = 24%%hours%% >> %RunBat%
echo if 1%%ms%% lss 100 set ms=0%%ms%% >> %RunBat%
echo set ^/a totalsecs = %%hours%%*3600 + %%mins%%*60 + %%secs%% >> %RunBat%
echo echo Time Elapsed %%hours%%:%%mins%%:%%secs%%.%%ms%% (%%totalsecs%%.%%ms%%s total) ^> %TimeElapsed% >> %RunBat%
echo echo Time Elapsed %%hours%%:%%mins%%:%%secs%%.%%ms%% (%%totalsecs%%.%%ms%%s total) >> %RunBat%
echo TIMEOUT ^/T 5 ^/NOBREAK ^>nul 2^>^&1 >> %RunBat%



set "TimeLimt=8"
START "RunElder" cmd /C %RunBat%
TIMEOUT /T %TimeLimt% /NOBREAK >nul 2>&1
rem taskkill /FI "RunElder*" /T /F
taskkill /im %ExecFile% /f >nul 2>&1

echo.
rem if exist "%RunBat%" del %RunBat%
if exist "%OutputFile%" (
	where notepad++.exe >nul 2>&1
	IF ERRORLEVEL 1 (
		start notepad++.exe %OutputFile%
	) else (
		start notepad.exe %OutputFile%
	)
	echo Ok, saida gerada com sucesso.
	if exist "%TimeElapsed%" type %TimeElapsed%
	if exist "%TimeElapsed%" del %TimeElapsed%
	TIMEOUT /T %TimeLimt%  /NOBREAK >nul 2>&1
	echo.
	echo ###########################################################
	echo # 11^) Agora compare o conteudo gerado pelo seu programa   #
	echo #      com o apresentado no uDebug (Accepted Output^)      #
	echo ###########################################################
	echo.
	TIMEOUT /T 15  /NOBREAK >nul 2>&1
	rem pause
) else (
	cls
	echo.
	echo "******************************************************"
	echo "************** Houve algum problema! *****************"
	echo "******************************************************"
	pause
)

:errorHandling
