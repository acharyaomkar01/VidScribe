<!DOCTYPE html>
<html lang="en">
<head>
 
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="">
	<title>VidScribe - A Deep Learning System</title>
	 
	<link href="static/css/bootstrap.css" rel="stylesheet">
	 
	<link href="static/css/main.css" rel="stylesheet">
 
	<!--[if lt IE 9]>
	  <script src="static/js/html5shiv.js"></script>
	  <script src="static/js/respond.min.js"></script>
	<![endif]-->
 
	<link rel="shortcut icon" href="static/images/favicon.png">
	<script src="static/js/pace.js"></script>
 
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:300,600' rel='stylesheet' type='text/css'>
</head>

<body>
	<div class="preloader"></div>
	
	    <! -- ******************** MASTHEAD SECTION ******************** -->	
		<main id="top" class="masthead" role="main">
			<div class="container">
			<!--	<div class="logo"><img src="/static/images/video-icon.png" alt="logo"></a>	-->
				</div>
	 			<a href='/home'>
				<div class="logo"><img src="/static/images/logo_3.png" alt="logo"></a>	
				</a>				
				<br>
				<h1>Video description on the Go!</h1>
				<div class="row">
					<div class="col-md-6 col-sm-12 col-md-offset-3 subscribe">
						<form action = "/demo" method = "POST">
							<input class = "myButton" type="submit" name="demo" value="DEMO"/>
						</form>
						<span id="result" class="alertMsg"></span>
					<br/><br/><br/>
					</div>
	 			
					<a href="#explore" style = "color:white" class="scrollto">
					<p class="scrollto--arrow"><img src="static/images/scroll_down.png" alt="scroll down arrow"></p>
					</a>
			</div><! --/container -->
		</main><! --/main -->
 
	    <! -- ******************** TESTIMONIALS SECTION ******************** -->	 
		<main id="top" class="masthead2" role="main">

		<div id = explore class="section-title">
			<h2>Our Team</h2>
		</div>

		<section class="row features">
			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/ItsMe.jpg" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Omkar Acharya</h3>
						<p>acharyaomkar01@gmail.com</p>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->
 
			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/Parag.jpg" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Parag Ahivale</h3>
						<p>ahivale_parag@yahoo.com</p>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->
 
			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/Nehal.jpg" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Nehal Belgamwar</h3>
						<p>nehal.belgamwar@yahoo.com</p>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->
 
			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/gurnur.jpg" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Gurnur Wadhwani</h3>
						<p>gurnursmailbox@gmail.com</p>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->
		</section><! --/section -->
 

		<div id = explore class="section-title">
			<h2>Our Mentors</h2>
		</div>

		<section class="row features">
			<div class="col-sm-6 col-md-3">
			</div><! --/col-sm-6-->
 
			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/ParagSir.png" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Dr. Parag Kulkarni</h3>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->

			<div class="col-sm-6 col-md-3">
				<div class="thumbnail"> 
					<img src="static/images/SS_Sonawane.png" alt="analytics-icon" style="border-radius: 80px 80px 80px 80px; height: 100px; width: 100px">
					<div class="caption">
						<h3>Prof. S.S.Sonawane</h3>
					</div>
				</div><! --/thumbnail -->
			</div><! --/col-sm-6-->
 
			<div class="col-sm-6 col-md-3">
			</div><! --/col-sm-6-->


		</section>		
 
		<a href="#top" style = "color:white" class="scrollto">
		<p class="scrollto--arrow"><img src="static/images/scroll_up.png" alt="scroll up arrow"></p>
		</a>


		<div class="container">
			<section class="row breath">
				<div class="col-md-12 footerlinks">
					<p>&copy; 2016 Group-46.co. All Rights Reserved</p>
				</div>
			</section><! --/section -->
		</div><! --/container --> 
 
 
<script src="static/js/jquery.js"></script>
<script src="static/js/bootstrap.js"></script>
<script src="static/js/easing.js"></script>
<script src="static/js/nicescroll.js"></script>
 
 
<script>


 $(function() {
    $('.scrollto, .gototop').bind('click',function(event){
		 var $anchor = $(this);
		 $('html, body').stop().animate({
         scrollTop: $($anchor.attr('href')).offset().top
          }, 1500,'easeInOutExpo');
     event.preventDefault();
      });
  });
        

</script>
 
</body>
</html>
