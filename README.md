# Point News AI

Point News AI is a news aggregator that uses AI to enhance the online news experience. By using GPT-3 to condense articles
into just three bullet points, users can get straight to the point while scanning over 25 different major publications.

### Tech Specs
###### Back End
- Python
- Flask
- Redis
- Docker

###### Front End
- JavaScript
- React (HTML/CSS)

### Project Scope
This project is exclusively designed to be a learning experience and demonstration of knowledge, not intended for production or commercial use. All news articles are gathered using [Event Registry](https://eventregistry.org/) and summarized by prompting OpenAI's [GPT-3](https://openai.com/blog/gpt-3-apps/) API.


### Limitations
- Cost to use GPT-3 limits the amount of content that can be posted
- Few front end bugs:
  - Need to upgrade to production build
  - Pressing back causes components to disappear --> reloading the page makes them reappear 
  - Console Warning: "Each child in a list should have a unique "key" prop
  - Window resizing needs work

### Up Next 
- Automatic daily article updates
- Code comments for readability 
- Hosting with AWS

### Screenshots
<img width="874" alt="Screen Shot 2022-09-08 at 4 19 26 PM" src="https://user-images.githubusercontent.com/49734611/189242214-4f2db0b8-4f65-4182-8b39-e568ebdca17b.png">

