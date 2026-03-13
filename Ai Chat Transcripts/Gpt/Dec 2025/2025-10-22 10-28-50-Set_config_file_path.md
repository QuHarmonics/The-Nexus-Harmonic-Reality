# Set config file path

https://chat.openai.com/c/68f8ea19-7eec-8333-aed4-8a4339b4e248

## USER
can you set the file path for the config to match tis location?   Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData),

 "Logistix",

 "config.json");

;———————————————————————————————————————

; Setup configuration

;———————————————————————————————————————

[Setup]

WizardImageFile=D:\Deployment\Publish - Server Manager\branding\sidebar.bmp

WizardSmallImageFile=D:\Deployment\Publish - Server Manager\branding\logo_Cmw_icon-4.bmp

LicenseFile=D:\Deployment\Publish - Server Manager\license\license.txt

AppCopyright=Copyright (C) 2025 qu harmonics.

AppName=Logistix License Manager

AppVersion=1.0.0

DefaultDirName={pf}\LogistixsServerManager

DefaultGroupName=Logistxs

OutputBaseFilename=LogistixsServerManagerSetup

Compression=lzma

SolidCompression=yes

PrivilegesRequired=admin

SetupIconFile=D:\Deployment\Publish - Server Manager\branding\logo_Cmw_icon.ico

DisableWelcomePage=no

DisableDirPage=no



[Languages]

Name: "english"; MessagesFile: "compiler:Default.isl"



;———————————————————————————————————————

; Files to deploy

;———————————————————————————————————————

[Files]

; Explicitly include and rename the EXE

Source: "D:\Deployment\Publish - Server Manager\Logistix.LicenseManager.WinForm.exe"; DestDir: "{app}"; DestName: "LogistixsServerManager.exe"; Flags: ignoreversion

; Include all other dependencies

Source: "D:\Deployment\Publish - Server Manager\*.*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs



;———————————————————————————————————————

; Create Logs folder

;———————————————————————————————————————

[Dirs]

Name: "{app}\Logs"



;———————————————————————————————————————

; Shortcuts

;———————————————————————————————————————

[Icons]

Name: "{group}\Logistxs Server Manager"; Filename: "{app}\LogistixsServerManager.exe"; WorkingDir: "{app}"; 

Name: "{userdesktop}\Logistxs Server Manager"; Filename: "{app}\LogistixsServerManager.exe"; WorkingDir: "{app}"



;———————————————————————————————————————

; Uninstall: remove generated config and logs

;———————————————————————————————————————

[UninstallDelete]

Type: filesandordirs; Name: "{app}\Logs"

Type: dirifempty; Name: "{app}"



;———————————————————————————————————————

; Wizard pages & code

;———————————————————————————————————————

[Code]

var

  ApiPage: TInputQueryWizardPage;

  SignalRPage: TInputQueryWizardPage;



function InitializeSetup(): Boolean;

var

  UninstExe: string;

  ResultCode: Integer;

begin

  UninstExe := ExpandConstant('{uninstallexe}');

  if FileExists(UninstExe) then

    Exec(UninstExe, '/VERYSILENT /SUPPRESSMSGBOXES', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);

  Result := True;

end;



procedure InitializeWizard();

begin

  // ───── PAGE 1: API CONFIGURATION ─────

  ApiPage := CreateInputQueryPage(

    wpWelcome,

    'API Configuration',

    'Enter your API endpoints',

    'These values define the HTTP endpoints for Mobile and Local servers.'

  );



  ApiPage.Add('Mobile API URL:', False);

  ApiPage.Add('Mobile API Prefix:', False);

  ApiPage.Add('Local Server URL:', False);

  ApiPage.Add('Local Server Prefix:', False);



  ApiPage.Values[0] := 'https://MobileApi.Logistixs-solutions.com';

  ApiPage.Values[1] := ''; // Mobile prefix

  ApiPage.Values[2] := 'http://192.168.1.16:7071';

  ApiPage.Values[3] := 'api';



  // ───── PAGE 2: SIGNALR CONFIGURATION ─────

  SignalRPage := CreateInputQueryPage(

    ApiPage.ID,

    'SignalR Configuration',

    'Enter your WebSocket (SignalR) endpoints',

    'These values define the WebSocket (SignalR) URLs and ports for Mobile and Local servers.'

  );



  SignalRPage.Add('SignalR Mobile URL:', False);

  SignalRPage.Add('SignalR Mobile Port:', False);

  SignalRPage.Add('SignalR Local URL:', False);

  SignalRPage.Add('SignalR Local Port:', False);



  SignalRPage.Values[0] := 'wss://MobileApi.Logistixs-solutions.com';

  SignalRPage.Values[1] := '7071';

  SignalRPage.Values[2] := 'ws://192.168.1.16';

  SignalRPage.Values[3] := '7071';

end;



function NextButtonClick(CurPageID: Integer): Boolean;

begin

  Result := True;



  if CurPageID = ApiPage.ID then

  begin

    if (Trim(ApiPage.Values[0]) = '') or (Trim(ApiPage.Values[2]) = '') then

    begin

      MsgBox('Please fill in all API fields before continuing.', mbError, MB_OK);

      Result := False;

    end;

  end

  else if CurPageID = SignalRPage.ID then

  begin

    if (Trim(SignalRPage.Values[0]) = '') or (Trim(SignalRPage.Values[2]) = '') then

    begin

      MsgBox('Please fill in all SignalR fields before continuing.', mbError, MB_OK);

      Result := False;

    end;

  end;

end;



procedure CurStepChanged(CurStep: TSetupStep);

var

  JsonText, FilePath: string;

begin

  if CurStep <> ssPostInstall then Exit;



FilePath := ExpandConstant('{app}\config.json');



  // Build JSON configuration dynamically from wizard values

  JsonText :=

    '{' + #13#10 +

    '  "LocalSignalUri": "' + SignalRPage.Values[2] + '",' + #13#10 +

    '  "LocalSignalPort": "' + SignalRPage.Values[3] + '",' + #13#10 +

    '  "MobileSignalRUrl": "' + SignalRPage.Values[0] + '",' + #13#10 +

    '  "LocalAPIUri": "' + ApiPage.Values[2] + '",' + #13#10 +

    '  "LocalAPIPrefix": "' + ApiPage.Values[3] + '",' + #13#10 +

    '  "MobileAPIUri": "' + ApiPage.Values[0] + '",' + #13#10 +

    '  "MobileAPIPrefix": "' + ApiPage.Values[1] + '",' + #13#10 +

    '  "DeviceGUID": ""' + #13#10 +

    '}';



  SaveStringToFile(FilePath, JsonText, False);



end;


## ASSISTANT
To align your installer’s `[Code]` section so the config file is written to the correct per-user path —  
`%AppData%\Logistix\config.json` — simply change the assignment inside `CurStepChanged`:

```pascal
FilePath := ExpandConstant('{userappdata}\Logistix\config.json');
```

Optionally ensure the directory exists first:

```pascal
CreateDir(ExpandConstant('{userappdata}\Logistix'));
FilePath := ExpandConstant('{userappdata}\Logistix\config.json');
```

This corresponds to the same location produced in .NET by:
```csharp
Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData),
    "Logistix",
    "config.json"
);
```

✅ **Result:**  
Your Inno Setup script will now save the generated `config.json` into the current user’s  
`AppData\Roaming\Logistix` directory — matching your application’s runtime expectations.

