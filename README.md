
# Hot Wheels

Ramhacks 2019 second place winners

## Inspiration

CarMax has a problem with indicating to customers whether a car is available for purchase. We set out to find an effective and creative way to solve this problem.

## What it does

The application uses Augmented Reality on the CarMax mobile app to communicate to costumers that a car is available or not just by pointing their phone at it.

## How we built it

- The data for the vehicle locations are stored in a MongoDB cluster
- A backend flask app communicates with the database and creates endpoints for the frontend to get data from
- A mobile frontend (Made to be a CarMax app look-a-like) written in Unity uses the location of the cars and the user's location + direction to figure out which cars it's looking at. From there it can query the backend for the info on the cars

## Challenges we ran into

Augmented reality on the cars turned out to be a harder topic to tackle because of our limited supply of cars. During the process of finding replacements for the vehicles, we attempted to 3D scan toy hot wheels to use instead which took much longer than expected and required installing apps that weren't on the google play store.

## Accomplishments that we're proud of

After hours of troubleshooting, our team is incredibly proud of getting 3D scans of all mock vehicles we used. None of our members had ever used Unity before so on top of the 3D scans, all progress made on the unity side was met with great excitement.

## What we learned

We learned plenty of information about the process of 3D object detection, manipulation of multiple cameras in a unity scene, and how to have each other effectively work in a team. Our team had never been in a team together in a hackathon and we found interesting ways to stay focus and delegate work between us.

## What's next for Hot Wheels

Next, we take over the world?

