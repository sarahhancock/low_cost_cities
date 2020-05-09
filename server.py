from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 31
cities = [
    {
        "id": 1,
        "city": "Austin",
        "state": "Texas",
        "map": "https://maps.google.com/maps?q=ausin%20texas&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Austin is the state capital of Texas, an inland city bordering the Hill Country region. Home to the University of Texas flagship campus, Austin is known for its eclectic live-music scene centered around country, blues and rock. Its many parks and lakes are popular for hiking, biking, swimming and boating. South of the city, Formula One's Circuit of the Americas raceway has hosted the United States Grand Prix.",
        "avg_home_price": 394095,
        "features": [
            {"name":"music scene", "mark_as_deleted": 0},
            {"name":"parks", "mark_as_deleted": 0},
            {"name":"lakes", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Austin_August_2019_19_%28skyline_and_Lady_Bird_Lake%29.jpg/560px-Austin_August_2019_19_%28skyline_and_Lady_Bird_Lake%29.jpg"
    },
    {
        "id": 2,
        "city": "Denver",
        "state": "Colorado",
        "map": "https://maps.google.com/maps?q=denver%20colorado&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Denver, the capital of Colorado, is an American metropolis dating to the Old West era. Larimer Square, the city’s oldest block, features landmark 19th-century buildings. Museums include the Denver Art Museum, an ultramodern complex known for its collection of indigenous works, and the mansion of famed Titanic survivor Molly Brown. Denver is also a jumping-off point for ski resorts in the nearby Rocky Mountains.",
        "avg_home_price": 454940,
        "features": [
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Denver_skyline.jpg/532px-Denver_skyline.jpg"
    },
    {
        "id": 3,
        "city": "Colorado Springs",
        "state": "Colorado",
        "map": "https://maps.google.com/maps?q=colorado%20springs&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Colorado Springs, at an elevation of 6,035 ft., is a city in Colorado at the eastern foot of the Rocky Mountains. It lies near glacier-carved Pikes Peak, a landmark in Pike National Forest with hiking trails and a cog railway leading to its 14,114-ft. summit. The city's Garden of the Gods park features iconic red-sandstone formations and mountain views.",
        "avg_home_price": 316396,
        "features": [
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/CC_COSPRINGS.jpg/600px-CC_COSPRINGS.jpg"
    },
    {
        "id": 4,
        "city": "Fayetteville",
        "state": "Arkansas",
        "map": "https://maps.google.com/maps?q=fayetteville%20arkansas&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Fayetteville is a city in northwest Arkansas. Near the University of Arkansas campus, the Clinton House Museum was the first home of Bill and Hillary Clinton. Vintage and modern airplanes are on display in a hangar at the Arkansas Air and Military Museum. To the west, Prairie Grove Battlefield State Park was the site of a Civil War battle. Mount Sequoyah Woods Trail runs through a thick forest.",
        "avg_home_price": 218094,
        "features": [
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://moneydotcomvip.files.wordpress.com/2018/08/best-places-to-live-2018-45-fayetteville-arkansas.jpg?quality=85&w=1600"
    },
    {
        "id": 5,
        "city": "Des Moines",
        "state": "Iowa",
        "map": "https://maps.google.com/maps?q=des%20moines%20iowa&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Des Moines is the capital city of Iowa. The gold-domed Iowa State Capitol building is among the 19th- and early-20th-century landmarks of the East Village area. The Des Moines Art Center is noted for its contemporary collections and Pappajohn Sculpture Park. Local produce and live music are draws at the Downtown Farmers' Market. The Greater Des Moines Botanical Garden has outdoor plant displays and a geodesic dome.",
        "avg_home_price": 148040,
        "features":  [
            {"name":"state fair", "mark_as_deleted": 0},
            {"name":"Iowa caucus", "mark_as_deleted": 0}
            ],
        "photo": "https://d194ip2226q57d.cloudfront.net/images/TakeFridayOff_DesMoines_Skyline_COThe-GreaterDe.original.jpg"
    },
    {
        "id": 6,
        "city": "Saint Paul",
        "state": "Minnesota",
        "map": "https://maps.google.com/maps?q=saint%20paul%20minnesota&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Saint Paul, the state capital of Minnesota, forms the 'Twin Cities' with neighboring Minneapolis. It’s home to the Science Museum of Minnesota, with its dinosaur specimens and immersive theater. The Minnesota History Center has interactive exhibits about the region's history. Nearby is the beaux arts Cathedral of Saint Paul. The Cass Gilbert–designed Minnesota State Capitol features paintings of Civil War scenes.",
        "avg_home_price": 235706,
        "features": [
            {"name":"Mississippi River", "mark_as_deleted": 0},
            {"name":"urban", "mark_as_deleted": 0}
            ],
        "photo": "https://stmedia.stimg.co/ctyp_st-paul-skyline-boat.jpg?w=800"
    },
    {
        "id": 7,
        "city": "Raleigh",
        "state": "North Carolina",
        "map": "https://maps.google.com/maps?q=raleigh%20north%20carolina&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Raleigh is the capital city of North Carolina. It’s known for its universities, including North Carolina State University. The number of technology and scholarly institutions around Raleigh, Chapel Hill and Durham make the area known as the Research Triangle. The North Carolina State Capitol is a 19th-century Greek Revival–style building with a statue of George Washington dressed as a Roman general in its rotunda.",
        "avg_home_price": 284829,
        "features": [
            {"name":"oak trees", "mark_as_deleted": 0},
            {"name":"southern charm", "mark_as_deleted": 0}
            ],
        "photo": "https://cedarmanagementgroup.com/wp-content/uploads/2019/11/raleigh-nc-5472x2736.jpg"
    },
    {
        "id": 8,
        "city": "Huntsville",
        "state": "Alabama",
        "map": "https://maps.google.com/maps?q=huntsville&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "The high-tech city of Huntsville, which sprawls at the foot of a mountain in North Alabama, is equally at home in the 19th century or the 21st. Huntsville's tourist attractions reflect the heritage of Alabama's first English-speaking city, the strife of the American Civil War and the accomplishments of America's rocket scientists. The city is nicknamed 'The Rocket City' for its close history with U.S. space missions. Huntsville has been important in developing space technology since the 1950s.",
        "avg_home_price": 176407,
        "features": [
            {"name":"voted best affordable place to live by US News", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Downtown_Huntsville%2C_Alabama_cropped.jpg/560px-Downtown_Huntsville%2C_Alabama_cropped.jpg"
    },
    {
        "id": 9,
        "city": "Madison",
        "state": "Wisconsin",
        "map": "https://maps.google.com/maps?q=madison&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Madison, the capital city of Wisconsin, lies west of Milwaukee. It’s known for the domed Wisconsin State Capitol, which sits on an isthmus between lakes Mendota and Monona. The Wisconsin Historical Museum documents the state’s immigrant and farming history. The city's paved Capital City State Trail runs past Monona Terrace, a lakefront convention center designed by Frank Lloyd Wright.",
        "avg_home_price": 279583,
        "features": [
            {"name":"lake", "mark_as_deleted": 0},
            {"name":"music", "mark_as_deleted": 0},
            {"name":"cycling", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Madison_Picnic_Point.jpg/600px-Madison_Picnic_Point.jpg"
    },
    {
        "id": 10,
        "city": "Grand Rapids",
        "state": "Michigan",
        "map": "https://maps.google.com/maps?q=grand%20rapids&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Grand Rapids is a Michigan city on the Grand River, east of Lake Michigan. On the outskirts, the Frederik Meijer Gardens & Sculpture Park has a tropical conservatory and multiple gardens. Its art collection includes works by Auguste Rodin, Henry Moore and Ai Weiwei. Downtown, the Grand Rapids Art Museum spotlights Michigan artists in its rotating shows. Grand Rapids is known for many breweries dotted around town.",
        "avg_home_price": 181200,
        "features": [
            {"name":"breweries", "mark_as_deleted": 0},
            {"name":"furniture manufacturing", "mark_as_deleted": 0}
            ],
        "photo": "https://www.outfrontmedia.com/-/media/images/ofm/markets/grand-rapids/grand-rapids-hero.ashx"
    },
    {
        "id": 11,
        "city": "Asheville",
        "state": "North Carolina",
        "map": "https://maps.google.com/maps?q=Asheville%20North%20Carolina&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Asheville is a city in western North Carolina’s Blue Ridge Mountains. It’s known for a vibrant arts scene and historic architecture, including the dome-topped Basilica of Saint Lawrence. The vast 19th-century Biltmore estate displays artwork by masters like Renoir. The Downtown Art District is filled with galleries and museums, and in the nearby River Arts District, former factory buildings house artists' studios.",
        "avg_home_price": 304398,
        "features": [
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://www.areavibes.com/photos/places/asheville-nc-1200.jpg"
    },
    {
        "id": 12,
        "city": "Plano",
        "state": "Texas",
        "map": "https://maps.google.com/maps?q=Plano%20Texas&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Plano is a city in north Texas. The Heritage Farmstead Museum is a restored 19th-century farm with original tools and furniture, plus a replica 1895 schoolroom. The Interurban Railway Museum traces the history of the Texas Electric Railway, and has a vintage rail car. Trails wind through a nature preserve in Oak Point Park. Northeast of town is Southfork Ranch, made famous as the setting for the TV series “Dallas.”",
        "avg_home_price": 342581,
        "features": [
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"businesses", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Plano_Skyline.jpg/500px-Plano_Skyline.jpg"
    },
    {
        "id": 13,
        "city": "Greenville",
        "state": "South Carolina",
        "map": "https://maps.google.com/maps?q=" + "Greenville" + "%20" + "South Carolina" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Greenville is a city in South Carolina. It’s home to the Greenville County Museum of Art, with works by Southern artists spanning several centuries. Exhibits at the Upcountry History Museum tell the story of upstate South Carolina. Falls Park on the Reedy has riverside gardens, a suspension bridge and waterfall views. Multi-use trails wind around lakes and hills in Paris Mountain State Park, north of the city.",
        "avg_home_price": 203542,
        "features": [
            {"name":"nature", "mark_as_deleted": 0},
            {"name":"waterfalls", "mark_as_deleted": 0}
            ],
        "photo": "https://livability.com/sites/default/files/GreenvilleSC-Skyline.jpg"
    },
    {
        "id": 14,
        "city": "Charlotte",
        "state": "North Carolina",
        "map": "https://maps.google.com/maps?q=" + "Charlotte" + "%20" + "North Carolina" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Charlotte is a major city and commercial hub in North Carolina. Its modern city center (Uptown) is home to the Levine Museum of the New South, which explores post–Civil War history in the South, and hands-on science displays at Discovery Place. Uptown is also known for the NASCAR Hall of Fame, which celebrates the sport of auto racing through interactive exhibits and films.",
        "avg_home_price": 249707,
        "features": [
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"historic", "mark_as_deleted": 0}
            ],
        "photo": "https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1687,w_3000,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1547334836/190113-jones-charlotte-north-carolina-hero_pr59qz"
    },
    {
        "id": 15,
        "city": "Portland",
        "state": "Maine",
        "map": "https://maps.google.com/maps?q=" + "Portland" + "%20" + "Maine" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Portland is a city in the U.S. state of Maine, set on a peninsula extending into Casco Bay. The Old Port waterfront features working fishing wharves and converted warehouses with restaurants and shops. Nearby, the Western Promenade is a public park atop a bluff, offering river and mountain views. Its surrounding district, the West End, is full of Victorian-era homes, including the Victoria Mansion museum.",
        "avg_home_price": 330215,
        "features": [
            {"name":"waterfront", "mark_as_deleted": 0},
            {"name":"coastal", "mark_as_deleted": 0},
            {"name":"close to mountains", "mark_as_deleted": 0}
            ],
        "photo": "https://www.visitportland.com/pictures/headerpics/959.jpg"
    },
    {
        "id": 16,
        "city": "Salt Lake City",
        "state": "Utah",
        "map": "https://maps.google.com/maps?q=" + "Salt Lake City" + "%20" + "Utah" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Salt Lake City is the capital and most populous municipality of the U.S. state of Utah, as well as the seat of Salt Lake County, the most populous county in Utah. With an estimated population of 200,591 in 2018, the city is the core of the Salt Lake City metropolitan area, which has a population of 1,222,540. It is one of only two major urban areas in the Great Basin. The world headquarters of The Church of Jesus Christ of Latter-day Saints (LDS Church) is located in Salt Lake City.",
        "avg_home_price": 414515,
        "features": [
            {"name":"eclectic", "mark_as_deleted": 0},
            {"name":"nature", "mark_as_deleted": 0},
            {"name":"urban", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Salt_Lake_City_montage_19_July_2011.jpg/580px-Salt_Lake_City_montage_19_July_2011.jpg"
    },
    {
        "id": 17,
        "city": "Melbourne",
        "state": "Florida",
        "map": "https://maps.google.com/maps?q=" + "Melbourne" + "%20" + "Florida" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Melbourne is a Florida city southeast of Orlando. The Eau Gallie Arts District, on the Indian River Lagoon, is known for its galleries and Foosaner Art Museum. Period buildings include the Rossetter House Museum & Gardens, restored to its 1908 appearance. Across the lagoon, Howard E. Futch Memorial Park at Paradise Beach faces the Atlantic Ocean. North, Brevard Zoo features a kayak tour through an African habitat.",
        "avg_home_price": 243649,
        "features": [
            {"name":"beach", "mark_as_deleted": 0},
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Historic_Downtown_Melbourne.jpg/500px-Historic_Downtown_Melbourne.jpg"
    },
    {
        "id": 18,
        "city": "Phoenix",
        "state": "Arizona",
        "map": "https://maps.google.com/maps?q=" + "Phoenix" + "%20" + "Arizona" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Phoenix is the capital of the southwestern U.S. state of Arizona. Known for its year-round sun and warm temperatures, it anchors a sprawling, multicity metropolitan area known as the Valley of the Sun. It's known for high-end spa resorts, Jack Nicklaus–designed golf courses and vibrant nightclubs. Other highlights include the Desert Botanical Garden, displaying cacti and numerous native plants.",
        "avg_home_price": 263253,
        "features": [
            {"name":"warm", "mark_as_deleted": 0},
            {"name":"desert", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/PhoenixMontage02.jpg/600px-PhoenixMontage02.jpg"
    },
    {
        "id": 19,
        "city": "Albany",
        "state": "New York",
        "map": "https://maps.google.com/maps?q=" + "Albany" + "%20" + "New York" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Albany is the capital city of New York State. Downtown’s huge Empire State Plaza has reflecting pools, an art-filled underground shopping concourse and The Egg, a striking performing arts center. The plaza is bookended by the 1800s New York State Capitol and the New York State Museum, focusing on natural and cultural history. The Albany Institute of History and Art is famed for its Hudson River School paintings.",
        "avg_home_price": 187619,
        "features": [
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"education", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Albany_New_York_Compilation.jpg/500px-Albany_New_York_Compilation.jpg"
    },
    {
        "id": 20,
        "city": "Lexington",
        "state": "Kentucky",
        "map": "https://maps.google.com/maps?q=" + "Lexington" + "%20" + "Kentucky" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Lexington is a city in Kentucky. It’s known for horse farms and thoroughbred racetracks like Keeneland. The Kentucky Horse Park features the International Museum of the Horse, the Hall of Champions and many equine breeds. Ashland, the estate of 1800s politician Henry Clay, includes a mansion and formal garden. Clay is buried at the Lexington Cemetery, which has an arboretum, lakes and a Romanesque gatehouse.",
        "avg_home_price": 196685,
        "features": [
            {"name":"horses", "mark_as_deleted": 0},
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"trees", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/52/Lexington_montage.jpg"
    },
    {
        "id": 21,
        "city": "Winston-Salem",
        "state": "North Carolina",
        "map": "https://maps.google.com/maps?q=" + "Winston-Salem" + "%20" + "North Carolina" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Winston-Salem is a city in and the county seat of Forsyth County, North Carolina, United States.[3] With a 2018 estimated population of 246,328 it is the second largest municipality in the Piedmont Triad region, the fifth most populous city in North Carolina, the third largest urban area in North Carolina, and the eighty-ninth most populous city in the United States. With a metropolitan population of 676,673 it is the fourth largest metropolitan area in North Carolina. Winston-Salem is home to the tallest office building in the region, 100 North Main Street, formerly the Wachovia Building and now known locally as the Wells Fargo Center.",
        "avg_home_price": 149505,
        "features": [
            {"name":"arts", "mark_as_deleted": 0},
            {"name":"banks", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Winston-Salem_skyline.jpg/600px-Winston-Salem_skyline.jpg"
    },
    {
        "id": 22,
        "city": "Omaha",
        "state": "Nebraska",
        "map": "https://maps.google.com/maps?q=" + "Omaha" + "%20" + "Nebraska" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Omaha is a city in the U.S. state of Nebraska, on the Missouri River close to the Iowa border. A stop on the Lewis & Clark National Historic Trail, it's known for its pioneer history, museums and cultural centers. The Henry Doorly Zoo and Aquarium spearheads conservation work and features a big cat complex as well as indoor jungle, rainforest and desert habitats.",
        "avg_home_price": 193062,
        "features": [
            {"name":"waterfront", "mark_as_deleted": 0},
            {"name":"urban", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Heartland_of_America_Park%2C_Omaha%2C_Nebraska.jpg/500px-Heartland_of_America_Park%2C_Omaha%2C_Nebraska.jpg"
    },
    {
        "id": 23,
        "city": "Reno",
        "state": "Nevada",
        "map": "https://maps.google.com/maps?q=" + "Reno" + "%20" + "Nevada" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Reno is a city in the northwest section of the U.S. state of Nevada, approximately 22 miles (35 km) from Lake Tahoe, known as 'The Biggest Little City in the World'. Known for its casino & tourism industry, Reno is the county seat and largest city of Washoe County and sits in a high desert river valley at the foot of the Sierra Nevada and its downtown area (along with Sparks) occupies a valley informally known as the Truckee Meadows, which due to large-scale investments from Seattle & Bay Area companies such as Amazon, Tesla, Panasonic, Microsoft, Apple and Google has become a new major technology hub in the United States.",
        "avg_home_price": 389280,
        "features": [
            {"name":"casinos", "mark_as_deleted": 0},
            {"name":"tourism", "mark_as_deleted": 0},
            {"name":"technology", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Reno_skyline.JPG/500px-Reno_skyline.JPG"
    },
    {
        "id": 24,
        "city": "Fort Myers",
        "state": "Florida",
        "map": "https://maps.google.com/maps?q=" + "Fort Myers" + "%20" + "Florida" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Fort Myers or Ft. Myers, is the county seat and commercial center of Lee County, Florida, United States. It has grown rapidly in recent years. As of the 2010 census, the city population was 62,298 and in 2018 was estimated at 82,254. Fort Myers is a gateway to the Southwest Florida region and a major tourist destination within Florida. The winter estates of Thomas Edison ('Seminole Lodge') and Henry Ford ('The Mangoes') are major attractions. The city is named after Colonel Abraham Myers, the quartermaster general of the Confederate States Army.",
        "avg_home_price": 220603,
        "features": [
            {"name":"beach", "mark_as_deleted": 0},
            {"name":"palm trees", "mark_as_deleted": 0},
            {"name":"tourism", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Fort_Myers_FL_Downtown_HD_1933_crths_pano01.jpg/500px-Fort_Myers_FL_Downtown_HD_1933_crths_pano01.jpg"
    },
    {
        "id": 25,
        "city": "Pensacola",
        "state": "Florida",
        "map": "https://maps.google.com/maps?q=" + "Pensacola" + "%20" + "Florida" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Pensacola is the westernmost city in the Florida Panhandle, and the county seat of Escambia County, Florida. As of 2019, the population was estimated to be 52,713. Pensacola is the principal city of the Pensacola Metropolitan Area, which had an estimated 494,883 residents as of 2018. Pensacola is one of the largest metropolitan areas in the Gulf Coast region, the largest between New Orleans and Tampa.",
        "avg_home_price": 159556,
        "features": [
            {"name":"beach", "mark_as_deleted": 0},
            {"name":"nature", "mark_as_deleted": 0}
            ],
        "photo": "https://i.pinimg.com/originals/1c/46/7b/1c467bfb3b5931a7b352a9176edeb8de.jpg"
    },
    {
        "id": 26,
        "city": "Indianapolis",
        "state": "Indiana",
        "map": "https://maps.google.com/maps?q=" + "Indianapolis" + "%20" + "Indiana" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Indianapolis, often shortened to Indy, is the state capital and most populous city of the U.S. state of Indiana and the seat of Marion County. According to 2018 estimates from the U.S. Census Bureau, the consolidated population of Indianapolis and Marion County was 876,862. Indianapolis is home to two major league sports clubs, the Indiana Pacers of the National Basketball Association (NBA) and the Indianapolis Colts of the National Football League (NFL). It is home to a number of educational institutions, such as the University of Indianapolis, Butler University, Marian University, and Indiana University – Purdue University Indianapolis (IUPUI). The city's robust philanthropic community has supported several cultural assets, including the world's largest children's museum, one of the nation's largest privately funded zoos, historic buildings and sites, and public art.",
        "avg_home_price": 149854,
        "features": [
            {"name":"historic", "mark_as_deleted": 0},
            {"name":"education", "mark_as_deleted": 0},
            {"name":"art", "mark_as_deleted": 0}
            ],
        "photo": "https://www.nationsonline.org/gallery/USA/Indianapolis-seen-from-Wapahani-Trail.jpg"
    },
    {
        "id": 27,
        "city": "Fort Wayne",
        "state": "Indiana",
        "map": "https://maps.google.com/maps?q=" + "Fort Wayne" + "%20" + "Indiana" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Fort Wayne is a city in northeastern Indiana. The Foellinger-Freimann Botanical Conservatory has indoor tropical, desert and showcase gardens, plus outdoor areas. American painting and sculpture are the focus at Fort Wayne Museum of Art. The 1860 Cathedral of the Immaculate Conception has 19th-century stained glass. Animal habitats at Fort Wayne Children’s Zoo include an African savannah and an Indonesian rainforest.",
        "avg_home_price": 144660,
        "features": [
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"nearby nature", "mark_as_deleted": 0}
            ],
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Downtown_Fort_Wayne%2C_Indiana_Skyline_from_Old_Fort%2C_May_2014.jpg/532px-Downtown_Fort_Wayne%2C_Indiana_Skyline_from_Old_Fort%2C_May_2014.jpg"
    },
    {
        "id": 28,
        "city": "Lansing",
        "state": "Michigan",
        "map": "https://maps.google.com/maps?q=" + "Lansing" + "%20" + "Michigan" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Lansing is the capital city of Michigan. Dating to the 1870s, the Michigan State Capitol building features a cast-iron dome. The Impression 5 Science Center has interactive displays. The collection at the R.E. Olds Transportation Museum includes classic and contemporary Oldsmobile cars. The Potter Park Zoo houses endangered and threatened species such as Magellanic penguins, black rhinos and golden lion tamarins.",
        "avg_home_price": 96128,
        "features": [
            {"name":"education", "mark_as_deleted": 0},
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"museums", "mark_as_deleted": 0}
            ],
        "photo": "https://static.ebayinc.com/static/assets/Uploads/Stories/Articles/_resampled/ScaleWidthWyI4MDAiXQ/lansing1.jpg"
    },
    {
        "id": 29,
        "city": "Jacksonville",
        "state": "Florida",
        "map": "https://maps.google.com/maps?q=" + "Jacksonville" + "%20" + "Florida" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Jacksonville is a large city in northeastern Florida where the St. John’s River meets the Atlantic Ocean. A regional business center, it has many museums and cultural offerings. Swimming and surfing are popular at nearby barrier island beaches such as Jacksonville Beach and Neptune Beach. Championship golf courses in the area include Ponte Vedra Beach’s TPC Sawgrass, headquarters of the PGA Tour.",
        "avg_home_price": 190347,
        "features": [
            {"name":"beach", "mark_as_deleted": 0},
            {"name":"nature", "mark_as_deleted": 0},
            {"name":"business", "mark_as_deleted": 0}
            ],
        "photo": "https://www.northamerican.com/images/default-source/movingresourcesimages/jacksonville-florida.jpg?sfvrsn=86a94eef_0"
    },
    {
        "id": 30,
        "city": "Manchester",
        "state": "New Hampshire",
        "map": "https://maps.google.com/maps?q=" + "Manchester" + "%20" + "New Hampshire" + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": "Manchester is a city on the Merrimack River in southern New Hampshire. The Currier Museum of Art features works by major American and European artists. It also operates the Frank Lloyd Wright–designed Zimmerman House. In an old fabric mill, the Millyard Museum traces how the nearby Amoskeag Falls shaped the city and its textile industry. Trails in sprawling Derryfield Park lead to the 19th-century Weston Observatory.",
        "avg_home_price": 257342,
        "features": [
            {"name":"urban", "mark_as_deleted": 0},
            {"name":"youthful vibe", "mark_as_deleted": 1}
            ],
        "photo": "https://blog.unpakt.com/wp-content/uploads/2017/07/Manchester-79425321_l-Manchester-New-Hampshire-USA-Skyline-on-the-Merrimack-River.jpg"
    }
    ] 


@app.route('/')
def home():
   return render_template('home.html', cities = cities)

@app.route('/view/<id>')
def view(id=None):
    city_to_view = {}
    for city in cities:
        if str(city["id"]) == id:
            city_to_view = city
    return render_template('view.html', city = city_to_view)  

@app.route('/edit/<id>')
def edit(id=None):
    city_to_edit = {}
    for city in cities:
        if str(city["id"]) == id:
            city_to_edit = city
    return render_template('edit.html', city = city_to_edit) 

@app.route('/create')
def create():
   return render_template('create.html')

@app.route('/search', methods=['GET'])
def search():
    global cities
    search_term = request.args.get('q')
    search = search_term.lower()
    filtered_cities = []
    for city in cities:
        if city["state"].lower().find(search) != -1:
            filtered_cities.append(city)
        elif city["city"].lower().find(search) != -1:
            filtered_cities.append(city)
    return render_template('search_results.html', results = filtered_cities,search_term = search_term)

@app.route('/get_latest_entries', methods=['GET', 'POST'])
def get_latest_entries():
    global cities
    filtered_cities = cities[-9:]
    filtered_cities.reverse()
    return jsonify(latest_entries = filtered_cities)

@app.route('/delete_city', methods=['GET', 'POST'])
def delete_city():
    global cities
    id_to_delete = int(request.get_json())
    for city in cities:
        if city["id"] == id_to_delete:
            del cities[cities.index(city)]
    return jsonify(cities = cities)

@app.route('/delete_feature', methods=['GET', 'POST'])
def delete_feature():
    global cities
    data = request.get_json()
    city_id = int(data["city_id"])
    feature_id = int(data["feature_id"])
    for city in cities:
        if city["id"] == city_id:
            city["features"][feature_id]["mark_as_deleted"] = 1
    return jsonify(cities = cities)

@app.route('/undo_delete', methods=['GET', 'POST'])
def undo_delete():
    global cities
    data = request.get_json()
    city_id = int(data["city_id"])
    feature_id = int(data["feature_id"])
    for city in cities:
        if city["id"] == city_id:
            city["features"][feature_id]["mark_as_deleted"] = 0
    return jsonify(cities = cities)

@app.route('/new_city', methods=['GET', 'POST'])
def new_city():
    global cities
    global current_id
    city = request.get_json()
    city["id"] = current_id
    cities.append(city)
    new_id = current_id
    current_id += 1
    return jsonify(cities = cities, id = new_id)

@app.route('/change_description', methods=['GET', 'POST'])
def change_description():
    global cities
    data = request.get_json()
    new_description = data["new_description"]
    id_to_change = data["id_to_change"]
    for city in cities:
        if city["id"] == id_to_change:
            city["description"] = new_description
    return jsonify(cities = cities)

@app.route('/add_feature', methods=['GET', 'POST'])
def add_feature():
    global cities
    data = request.get_json()
    new_feature_name = data["new_feature"]
    id_to_change = data["id_to_change"]
    for city in cities:
        if city["id"] == id_to_change:
            new_feature = {"name": new_feature_name, "mark_as_deleted":0}
            city["features"].append(new_feature)
    return jsonify(cities = cities)

    

if __name__ == '__main__':
   app.run(debug = True)




