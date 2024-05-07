


 const form = document.querySelector('form');


 function formatTime(milliseconds) {
   const minutes = Math.floor(milliseconds / 60000);
   const seconds = ((milliseconds % 60000) / 1000).toFixed(0);
   return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
 }
 
 remfilters=document.getElementById('remfilters');
 function clearSearch() {
  document.getElementById("duration-filter").value = "";
  document.getElementById('explicit-filter').checked=false;
  document.getElementById('explicit-filter1').checked=false;
}

function clearexpl() {
  
  document.getElementById('explicit-filter').checked=false;
  
}
function clearexpl() {
  
  document.getElementById('explicit-filter').checked=false;
  document.getElementById('remfilters').checked=false;
  
}
function clearnonexpl() {
  document.getElementById('remfilters').checked=false;
  document.getElementById('explicit-filter1').checked=false;
}
form.addEventListener('submit', function(event) {
  event.preventDefault();
const durationFilter = form.elements['duration-filter'].value;
const filterExplicit = document.getElementById('explicit-filter');
const filterExplicit1 = document.getElementById('explicit-filter1');
if(filterExplicit.checked==true && durationFilter==='' && filterExplicit1.checked==false){
    remfilters.checked=false;
    
    i=0;
    
   
    const searchTerm = form.elements.term.value.toLowerCase();
    const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
    
    fetch(url)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        const results = data.results.filter(result => result.trackExplicitness !== "explicit"); // Filter out explicit content
        const resultsDiv = document.getElementById('search-results');
        
        // Clear any previous search results
        resultsDiv.innerHTML = '';
        
        let artistResults = [];
        let albumResults = [];
        let songResults = [];
        
        // Sort results by artist, album, then song
        results.forEach(function(result) {
          const artistName = result.artistName.toLowerCase();
          const albumName = result.collectionName.toLowerCase();
          const songName = result.trackName.toLowerCase();
          const resultDiv = document.createElement('div');
  
          // Check if search term is in artist/album/song name
          if (artistName.includes(searchTerm)) {
            artistResults.push(result);
          } else if (albumName.includes(searchTerm)) {
            if (!artistResults.includes(result)) {
              albumResults.push(result);
            }
          } else if (songName.includes(searchTerm)) {
            if (!artistResults.includes(result) && !albumResults.includes(result)) {
              songResults.push(result);
            }
          }
        });
        
        // Display artist results first
        artistResults.forEach(function(result) {
          i++;
          const resultDiv = document.createElement('div');
          resultDiv.innerHTML = `
          <h2>${result.trackName}</h2>
            <p>Artist: ${result.artistName}</p>
            <p>Album: ${result.collectionName}</p>
            <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
            <p>Explicit: ${result.trackExplicitness}</p>
  
            <img src="${result.artworkUrl100}">
            <audio src="${result.previewUrl}" controls></audio>
          `;
          resultsDiv.appendChild(resultDiv);
        });
        
        // Display album results next
        albumResults.forEach(function(result) {
          i++;
          const resultDiv = document.createElement('div');
          resultDiv.innerHTML = `
          <h2>${result.trackName}</h2>
            <p>Artist: ${result.artistName}</p>
            <p>Album: ${result.collectionName}</p>
            <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
            <p>Explicit: ${result.trackExplicitness}</p>
  
            <img src="${result.artworkUrl100}">
            <audio src="${result.previewUrl}" controls></audio>
          `;
          resultsDiv.appendChild(resultDiv);
        });
        
        // Display song results last
         songResults.forEach(function(result) {
           i++;
           const resultDiv = document.createElement('div');
           resultDiv.innerHTML = `
            
             <h2>${result.trackName}</h2>
             <p>Artist: ${result.artistName}</p>
             <p>Album: ${result.collectionName}</p>
             <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
             <p>Explicitness: ${result.trackExplicitness}</p>
             <img src="${result.artworkUrl100}">
             <audio src="${result.previewUrl}" controls></audio>
           `;
           resultsDiv.appendChild(resultDiv);
         });
         
         // Display error message if no results found
         // Display error message if no results found
        if (results.length == 0 || i==0) {
          const resultDiv = document.createElement('div');
          resultDiv.textContent = "No Results Found";
          resultsDiv.appendChild(resultDiv);
        }

       })
       .catch(function(error) {
         console.log(error);
       });
    
  
     
}
else if(!filterExplicit.checked==true && durationFilter==='' && filterExplicit1.checked==false){
  remfilters.checked=false;
   i=0;
   const searchTerm = form.elements.term.value.toLowerCase();
   const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
   
   fetch(url)
     .then(function(response) {
       return response.json();
     })
     .then(function(data) {
       const results = data.results;
       const resultsDiv = document.getElementById('search-results');
       
       // Clear any previous search results
       resultsDiv.innerHTML = '';
       
       let artistResults = [];
       let albumResults = [];
       let songResults = [];
       
       // Sort results by artist, album, then song
       results.forEach(function(result) {
         const artistName = result.artistName.toLowerCase();
         const albumName = result.collectionName.toLowerCase();
         const songName = result.trackName.toLowerCase();
         const resultDiv = document.createElement('div');
 
         // Check if search term is in artist/album/song name
         if (artistName.includes(searchTerm)) {
           artistResults.push(result);
         } else if (albumName.includes(searchTerm)) {
           if (!artistResults.includes(result)) {
             albumResults.push(result);
           }
         } else if (songName.includes(searchTerm)) {
           if (!artistResults.includes(result) && !albumResults.includes(result)) {
             songResults.push(result);
           }
         }
       });
       
       // Display artist results first
       artistResults.forEach(function(result) {
        i++;
         const resultDiv = document.createElement('div');
         resultDiv.innerHTML = `
         <h2>${result.trackName}</h2>
           <p>Artist: ${result.artistName}</p>
           <p>Album: ${result.collectionName}</p>
           <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
           <p>Explicitness: ${result.trackExplicitness}</p>
           <img src="${result.artworkUrl100}">
           <audio src="${result.previewUrl}" controls></audio>
         `;
         resultsDiv.appendChild(resultDiv);
       });
       
       // Display album results next
       albumResults.forEach(function(result) {
        i++;
         const resultDiv = document.createElement('div');
         resultDiv.innerHTML = `
         <h2>${result.trackName}</h2>
           <p>Artist: ${result.artistName}</p>
           <p>Album: ${result.collectionName}</p>
           <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
           <p>Explicitness: ${result.trackExplicitness}</p>
           <img src="${result.artworkUrl100}">
           <audio src="${result.previewUrl}" controls></audio>
         `;
         resultsDiv.appendChild(resultDiv);
       });
       
       // Display song results last
       songResults.forEach(function(result) {
        i++;
         const resultDiv = document.createElement('div');
         resultDiv.innerHTML = `
           <h2>${result.trackName}</h2>
           <p>Artist: ${result.artistName}</p>
           <p>Album: ${result.collectionName}</p>
           <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
           <p>Explicitness: ${result.trackExplicitness}</p>
           <img src="${result.artworkUrl100}">
           <audio src="${result.previewUrl}" controls></audio>
         `;
         resultsDiv.appendChild(resultDiv);
       });
       
       // Display error message if no results found
       // Display error message if no results found
      if (results.length === 0 || i==0) {
        const resultDiv = document.createElement('div');
        resultDiv.textContent = "No Results Found";
        resultsDiv.appendChild(resultDiv);
      }

     })
     .catch(function(error) {
       console.log(error);
     });
   
}
else if(durationFilter !== '' && filterExplicit.checked==true && filterExplicit1.checked==false){
  remfilters.checked=false;
  document.getElementById('explicit-filter1').checked=false;
  i=0;
  const searchTerm = form.elements.term.value.toLowerCase();
  const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
  
  fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      
      const resultsDiv = document.getElementById('search-results');
      const results = data.results.filter(result => result.trackExplicitness !== "explicit"); // Filter out explicit content
      
      
      // Clear any previous search results
      resultsDiv.innerHTML = '';
      
      let artistResults = [];
      let albumResults = [];
      let songResults = [];
      
      // Sort results by artist, album, then song
      results.forEach(function(result) {
        const artistName = result.artistName.toLowerCase();
        const albumName = result.collectionName.toLowerCase();
        const songName = result.trackName.toLowerCase();
        const duration = result.trackTimeMillis / 1000 / 60;
        const resultDiv = document.createElement('div');
        if (duration < durationFilter || durationFilter === '') {
          // Check if search term is in artist/album/song name
          if (artistName.includes(searchTerm)) {
            artistResults.push(result);
          } else if (albumName.includes(searchTerm)) {
            if (!artistResults.includes(result)) {
              albumResults.push(result);
            }
          } else if (songName.includes(searchTerm)) {
            if (!artistResults.includes(result) && !albumResults.includes(result)) {
              songResults.push(result);
            }
          }
        }
      });
      
      
      // Display artist results first
      artistResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display album results next
      albumResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display song results last
      songResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
          <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display error message if no results found
      // Display error message if no results found
    if (results.length === 0 || i==0) {
      const resultDiv = document.createElement('div');
      resultDiv.textContent = "No Results Found";
      resultsDiv.appendChild(resultDiv);
    }

    })
    .catch(function(error) {
      console.log(error);
    });

}
else if(durationFilter!=='' && filterExplicit.checked==false && filterExplicit1.checked==false){
  remfilters.checked=false;
  i=0;
  const searchTerm = form.elements.term.value.toLowerCase();
  const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
  
  fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      const results = data.results;
      const resultsDiv = document.getElementById('search-results');
      
      // Clear any previous search results
      resultsDiv.innerHTML = '';
      
      let artistResults = [];
      let albumResults = [];
      let songResults = [];
      
      // Sort results by artist, album, then song
      results.forEach(function(result) {
        const artistName = result.artistName.toLowerCase();
        const albumName = result.collectionName.toLowerCase();
        const songName = result.trackName.toLowerCase();
        const duration = result.trackTimeMillis / 1000 / 60;
        const resultDiv = document.createElement('div');
        if (duration < durationFilter || durationFilter === '') {
          // Check if search term is in artist/album/song name
          if (artistName.includes(searchTerm)) {
            artistResults.push(result);
          } else if (albumName.includes(searchTerm)) {
            if (!artistResults.includes(result)) {
              albumResults.push(result);
            }
          } else if (songName.includes(searchTerm)) {
            if (!artistResults.includes(result) && !albumResults.includes(result)) {
              songResults.push(result);
            }
          }
        }
      });
      
      
      // Display artist results first
      artistResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display album results next
      albumResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display song results last
      songResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
          <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display error message if no results found
      // Display error message if no results found
    if (results.length === 0 || i==0) {
      const resultDiv = document.createElement('div');
      resultDiv.textContent = "No Results Found";
      
      
      resultsDiv.appendChild(resultDiv);
    }

    })
    .catch(function(error) {
      console.log(error);
    });
}

else if(durationFilter !== '' && filterExplicit1.checked==true && filterExplicit.checked==false){
  remfilters.checked=false;
  
  i=0;
  const searchTerm = form.elements.term.value.toLowerCase();
  const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
  
  fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      
      const resultsDiv = document.getElementById('search-results');
      const results = data.results.filter(result => result.trackExplicitness === "explicit");
 // Filter out explicit content
      
      
      // Clear any previous search results
      resultsDiv.innerHTML = '';
      
      let artistResults = [];
      let albumResults = [];
      let songResults = [];
      
      // Sort results by artist, album, then song
      results.forEach(function(result) {
        const artistName = result.artistName.toLowerCase();
        const albumName = result.collectionName.toLowerCase();
        const songName = result.trackName.toLowerCase();
        const duration = result.trackTimeMillis / 1000 / 60;
        const resultDiv = document.createElement('div');
        if (duration < durationFilter || durationFilter === '') {
          // Check if search term is in artist/album/song name
          if (artistName.includes(searchTerm)) {
            artistResults.push(result);
          } else if (albumName.includes(searchTerm)) {
            if (!artistResults.includes(result)) {
              albumResults.push(result);
            }
          } else if (songName.includes(searchTerm)) {
            if (!artistResults.includes(result) && !albumResults.includes(result)) {
              songResults.push(result);
            }
          }
        }
      });
      
      
      // Display artist results first
      artistResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display album results next
      albumResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display song results last
      songResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
          <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicitness: ${result.trackExplicitness}</p>
          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display error message if no results found
      // Display error message if no results found
    if (results.length === 0 || i==0) {
      const resultDiv = document.createElement('div');
      resultDiv.textContent = "No Results Found";
      resultsDiv.appendChild(resultDiv);
    }
    
    
    })
    .catch(function(error) {
      console.log(error);
    });

}
else if(filterExplicit.checked==false && durationFilter==='' && filterExplicit1.checked==true){
  remfilters.checked=false;
  
  i=0;
  
 
  const searchTerm = form.elements.term.value.toLowerCase();
  const url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;
  
  fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      const results = data.results.filter(result => result.trackExplicitness === "explicit"); // Filter out explicit content
      const resultsDiv = document.getElementById('search-results');
      
      // Clear any previous search results
      resultsDiv.innerHTML = '';
      
      let artistResults = [];
      let albumResults = [];
      let songResults = [];
      
      // Sort results by artist, album, then song
      results.forEach(function(result) {
        const artistName = result.artistName.toLowerCase();
        const albumName = result.collectionName.toLowerCase();
        const songName = result.trackName.toLowerCase();
        const resultDiv = document.createElement('div');

        // Check if search term is in artist/album/song name
        if (artistName.includes(searchTerm)) {
          artistResults.push(result);
        } else if (albumName.includes(searchTerm)) {
          if (!artistResults.includes(result)) {
            albumResults.push(result);
          }
        } else if (songName.includes(searchTerm)) {
          if (!artistResults.includes(result) && !albumResults.includes(result)) {
            songResults.push(result);
          }
        }
      });
      
      // Display artist results first
      artistResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicit: ${result.trackExplicitness}</p>

          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display album results next
      albumResults.forEach(function(result) {
        i++;
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
        <h2>${result.trackName}</h2>
          <p>Artist: ${result.artistName}</p>
          <p>Album: ${result.collectionName}</p>
          <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
          <p>Explicit: ${result.trackExplicitness}</p>

          <img src="${result.artworkUrl100}">
          <audio src="${result.previewUrl}" controls></audio>
        `;
        resultsDiv.appendChild(resultDiv);
      });
      
      // Display song results last
       songResults.forEach(function(result) {
         i++;
         const resultDiv = document.createElement('div');
         resultDiv.innerHTML = `
          
           <h2>${result.trackName}</h2>
           <p>Artist: ${result.artistName}</p>
           <p>Album: ${result.collectionName}</p>
           <p>Duration: ${formatTime(result.trackTimeMillis)}</p>
           <p>Explicitness: ${result.trackExplicitness}</p>
           <img src="${result.artworkUrl100}">
           <audio src="${result.previewUrl}" controls></audio>
         `;
         resultsDiv.appendChild(resultDiv);
       });
       
       // Display error message if no results found
       // Display error message if no results found
      if (results.length == 0 || i==0) {
        const resultDiv = document.createElement('div');
        resultDiv.textContent = "No Results Found";
        resultsDiv.appendChild(resultDiv);
      }

     })
     .catch(function(error) {
       console.log(error);
     });
  

   
}


});
