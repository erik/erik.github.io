$.getJSON("https://api.github.com/users/boredomist/repos?callback=?",
          function(data) {
              repos = data.data.sort(function(a, b) {
                  return Date.parse(b.pushed_at) - Date.parse(a.pushed_at);
              }).slice(0, 10);

              $.each(repos, function(i, repo) {
                  $("#gh").find("tbody")
                      .append($('<tr>')
                              .append($('<td>')
                                      .append($('<a>')
                                              .attr("href", repo.url)
                                              .text(repo.name)))
                              .append($('<td>')
                                      .text(repo.description)));
              });
          });
