{% extends 'UserInterface/base.html' %}


{% block title %} Articles {% endblock title %} 


{% block content %} 
<style>

  a{
    color: black !important;
  }
  
  
</style>

  <main class="my-5">
    <div class="container">
      <!--Section: Content-->
      <section class="text-center">
        <h4 class="mb-5"><strong>Latest posts</strong></h4>
        
     
    <div class="row">
    {% for article in announcements %}
      

   
 <div class="col-lg-4 col-md-12 mb-4">
   <div class="card">
     <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
       <img src="https://scontent.fmnl30-1.fna.fbcdn.net/v/t39.30808-6/363959470_268002949410153_908093610336867492_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFdYJSz7SmwqFstpjOgmmc1oqOXGFHttKmio5cYUe20qShvZz0vxfCrTMGM82k_O-HvuD8M6NmJZ8TISy_e_mtL&_nc_ohc=w0mXcFtryrQAX-Pn4Y2&_nc_ht=scontent.fmnl30-1.fna&oh=00_AfBRqbaGhoEMITXawykggrYr0lLt75w-sdCmqJwgOMB9lw&oe=6539C071" class="img-fluid" />
       <a href="#!">
         <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
       </a>
     </div>
     <div class="card-body">
       <h5 class="card-title">{{article.title}}</h5>
       <p class="card-text">
         {{article.content |truncatewords:16  }}
       </p>
       <button hx-get="/articles/view_article/{{article.id}}" hx-trigger = 'click' hx-target = 'body' class="btn btn-primary">Read</button>
     </div>
   </div>


 </div>
 

 {% if forloop.counter|divisibleby:3 %}
    </div>
    <div class="row">
 {% endif %}

    {% endfor %}

      
      </section>
      <!--Section: Content-->

      <!-- Pagination -->
      <nav class="my-4" aria-label="...">
        <ul class="pagination pagination-circle justify-content-center">
          <li class="page-item">
            <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
          </li>
          <li class="page-item active"><a class="page-link" href="#">1</a></li>
          <li class="page-item" aria-current="page">
            <a class="page-link" href="#">2 <span class="sr-only"></span></a>
          </li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item">
            <a class="page-link" href="#">Next</a>
          </li>
        </ul>
      </nav>
    </div>
  </main>
 
 
 
    



{% endblock %}



    <table class="table mt-5 mt-5 font-monospace">
        <thead>
            <tr >
                <th  >
                    Title
                </th>
                <th>
                    Author  
                </th>
            </tr>


            <tbody>
                {% for i in announcements %}
                    <tr>
                        <td id = {{i.id}} ondblclick="clicked(this)">{{i.title}}</td>
                        <td>{{i.author}}</td>

                    </tr>

                {% endfor %}
            </tbody>
        </thead>



    </table>


<main class="mt-5">
<div class="container">
  <!--Section: Content-->
  <section>
    <div class="row">
      <div class="col-md-6 gx-5 mb-4">
        <div class="bg-image hover-overlay ripple shadow-2-strong" data-mdb-ripple-color="light">
          <img src="https://mdbootstrap.com/img/new/slides/031.jpg" class="img-fluid" />
          <a href="#!">
            <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
          </a>
        </div>
      </div>

      <div class="col-md-6 gx-5 mb-4">
        <h4><strong>Facilis consequatur eligendi</strong></h4>
        <p class="text-muted">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis consequatur
          eligendi quisquam doloremque vero ex debitis veritatis placeat unde animi laborum
          sapiente illo possimus, commodi dignissimos obcaecati illum maiores corporis.
        </p>
        <p><strong>Doloremque vero ex debitis veritatis?</strong></p>
        <p class="text-muted">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod itaque voluptate
          nesciunt laborum incidunt. Officia, quam consectetur. Earum eligendi aliquam illum
          alias, unde optio accusantium soluta, iusto molestiae adipisci et?
        </p>
      </div>
    </div>
  </section>
  <!--Section: Content-->

  <hr class="my-5" />

  <!--Section: Content-->
  <section class="text-center">
    <h4 class="mb-5"><strong>Facilis consequatur eligendi</strong></h4>

    <div class="row">
      <div class="col-lg-4 col-md-12 mb-4">
        <div class="card">
          <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
            <img src="https://mdbootstrap.com/img/new/standard/nature/184.jpg" class="img-fluid" />
            <a href="#!">
              <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
            </a>
          </div>
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk of the
              card's content.
            </p>
            <a href="#!" class="btn btn-primary">Button</a>
          </div>
        </div>
      </div>

      <div class="col-lg-4 col-md-6 mb-4">
        <div class="card">
          <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
            <img src="https://mdbootstrap.com/img/new/standard/nature/023.jpg" class="img-fluid" />
            <a href="#!">
              <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
            </a>
          </div>
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk of the
              card's content.
            </p>
            <a href="#!" class="btn btn-primary">Button</a>
          </div>
        </div>
      </div>

      <div class="col-lg-4 col-md-6 mb-4">
        <div class="card">
          <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
            <img src="https://mdbootstrap.com/img/new/standard/nature/111.jpg" class="img-fluid" />
            <a href="#!">
              <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
            </a>
          </div>
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk of the
              card's content.
            </p>
            <a href="#!" class="btn btn-primary">Button</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!--Section: Content-->

  <hr class="my-5" />

  <!--Section: Content-->
  <section class="mb-5">
    <h4 class="mb-5 text-center"><strong>Facilis consequatur eligendi</strong></h4>

    <div class="row d-flex justify-content-center">
      <div class="col-md-6">
        <form>
          <!-- 2 column grid layout with text inputs for the first and last names -->
          <div class="row mb-4">
            <div class="col">
              <div class="form-outline">
                <input type="text" id="form3Example1" class="form-control" />
                <label class="form-label" for="form3Example1">First name</label>
              </div>
            </div>
            <div class="col">
              <div class="form-outline">
                <input type="text" id="form3Example2" class="form-control" />
                <label class="form-label" for="form3Example2">Last name</label>
              </div>
            </div>
          </div>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <input type="email" id="form3Example3" class="form-control" />
            <label class="form-label" for="form3Example3">Email address</label>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input type="password" id="form3Example4" class="form-control" />
            <label class="form-label" for="form3Example4">Password</label>
          </div>

          <!-- Checkbox -->
          <div class="form-check d-flex justify-content-center mb-4">
            <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3" checked />
            <label class="form-check-label" for="form2Example3">
              Subscribe to our newsletter
            </label>
          </div>

          <!-- Submit button -->
          <button type="submit" class="btn btn-primary btn-block mb-4">
            Sign up
          </button>

          <!-- Register buttons -->
          <div class="text-center">
            <p>or sign up with:</p>
            <button type="button" class="btn btn-primary btn-floating mx-1">
              <i class="fab fa-facebook-f"></i>
            </button>

            <button type="button" class="btn btn-primary btn-floating mx-1">
              <i class="fab fa-google"></i>
            </button>

            <button type="button" class="btn btn-primary btn-floating mx-1">
              <i class="fab fa-twitter"></i>
            </button>

            <button type="button" class="btn btn-primary btn-floating mx-1">
              <i class="fab fa-github"></i>
            </button>
          </div>
        </form>
      </div>
    </div>
  </section>
  <!--Section: Content-->
</div>
</main>




<nav class="navbar navbar-fixed-top navbar-expand-lg navbar-dark d-none d-lg-block" style="z-index: 2000;">
  <div class="container-fluid">
    <!-- Navbar brand -->
    <a class="navbar-brand nav-link" target="_blank" href="/">
      <h3>Domini Xode</h3>
    </a>
    <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarExample01"
      aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
      <i class="fas fa-bars"></i>
    </button>
    <div class="collapse navbar-collapse" id="navbarExample01">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">


        <li class="nav-item active">
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="/articles" rel="nofollow"
            target="_blank"> Articles </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" target="_blank"> Events</a>
        </li>

        <li class="nav-item">
          <a href="/about_us" class="nav-link">About Us</a>
        </li>

        <li class="nav-item">
          <a href="/contact_us" class="nav-link">Contact Us</a>
        </li>
      </ul>

      <ul class="navbar-nav list-inline">
        <!-- Icons -->
     
        <li class="">
          <a class="nav-link" href="https://www.facebook.com/sdcadominixode" rel="nofollow" target="_blank">
            <i class="fab fa-facebook-f"></i>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/definitelynotanassassin" rel="nofollow" target="_blank">
            <i class="fab fa-github"></i>
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!--Footer-->
<footer class="bg-light text-lg-start">
<div class="py-4 text-center">
  <a role="button" class="btn btn-primary btn-lg m-2"
    href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA" rel="nofollow" target="_blank">
    Learn Bootstrap 5
  </a>
  <a role="button" class="btn btn-primary btn-lg m-2" href="https://mdbootstrap.com/docs/standard/" target="_blank">
    Download MDB UI KIT
  </a>
</div>

<hr class="m-0" />

<div class="text-center py-4 align-items-center">
  <p>Follow MDB on social media</p>
  <a href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA" class="btn btn-primary m-1" role="button"
    rel="nofollow" target="_blank">
    <i class="fab fa-youtube"></i>
  </a>
  <a href="https://www.facebook.com/mdbootstrap" class="btn btn-primary m-1" role="button" rel="nofollow"
    target="_blank">
    <i class="fab fa-facebook-f"></i>
  </a>
  <a href="https://twitter.com/MDBootstrap" class="btn btn-primary m-1" role="button" rel="nofollow"
    target="_blank">
    <i class="fab fa-twitter"></i>
  </a>
  <a href="https://github.com/mdbootstrap/mdb-ui-kit" class="btn btn-primary m-1" role="button" rel="nofollow"
    target="_blank">
    <i class="fab fa-github"></i>
  </a>
</div>

<!-- Copyright -->
<div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
  © 2020 Copyright:
  <a class="text-dark" href="https://mdbootstrap.com/">MDBootstrap.com</a>
</div>
<!-- Copyright -->
</footer>
