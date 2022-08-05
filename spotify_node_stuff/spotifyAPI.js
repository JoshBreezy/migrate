import accessToken from './web-api-auth-examples/authorization_code/auth.js';
var Spotify = require('spotify-web-api-js');
var s = new Spotify();

s.setAccessToken(accessToken);

s.getUserPlaylists()
.then(
  function (data) {
    console.log('User playlists', data);
  },
  function (err) {
    console.error(err);
  }
);