import { error } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export function GET({ url }) {
  const data = {
    "key": "value",
  };

  //throw error(400, 'min and max must be numbers, and min must be less than max');
 
  return new Response(String(JSON.stringify(data)));
}