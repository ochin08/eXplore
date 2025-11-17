





// 1.) OR opeator
let hasTicket = true;
let isVIP = true;

if (hasTicket || isVIP) {
  console.log("Makakapasok ka.");
} else {
  console.log("Walang access.");
}



// 2.) AND operator
let age = 25;
let hasID = true;

if (age >= 18 && hasID) {
  console.log("Pwede kang pumasok.");
} else {
  console.log("Hindi ka pwede.");
}


// 3.) NOT operator
let isLoggedIn = false;

if (!isLoggedIn) {
  console.log("Kailangan mong mag-login.");
}