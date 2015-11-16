<!-- login.html -- authenticate users via Google -->
<!DOCTYPE html>
<html>
<body>

<!-- Basic profile -->
<h1>Display your Google profile</h1>
<a href="https://accounts.google.com/o/oauth2/auth?scope={{scope1}}&state=%2Fprofile&redirect_uri=http%3A%2F%2F{{addr}}:{{port}}%2Fauth.html&response_type=token&client_id={{cid}}"> Login </a>
<p>Click the link above to retrieve your account information</p>

<h1>Display your Google profile with Email Address</h1>
<a href="https://accounts.google.com/o/oauth2/auth?scope={{scope2}}&state=%2Fprofile&redirect_uri=http%3A%2F%2F{{addr}}:{{port}}%2Fauth.html&response_type=token&client_id={{cid}}"> Login </a>
<p>Click the link above to retrieve your profile information including email address</p>

<h1>Upload your Google profile to Google Drive</h1>
<a href="http://{{addr}}:{{port}}/drive.html"> Upload </a>
<p>Click the link above to upload your profile information to Google Drive</p>

</body>
</html>
