import { json } from "stream/consumers";

type CacheEntry = {
    url : string,
    ttl : number,
    result : any,
}

const cache : {[key:string]: CacheEntry} = {};

const fetcher = async function<Type>(url : string, ...args:any) : Promise<Type> {
    if(url in cache){
        const entry = cache[url];
        if(Date.now() < entry.ttl){
            return new Promise<Type>((resolve) => {
                resolve(entry.result);
            })
        }
    }
    const ttl = args.ttl || 1;
    return new Promise<Type>(resolve => {
        fetch(url, args).then(res => 
            res.json().then((data: Type) => {
                cache[url] = {
                    url,
                    ttl: new Date().getTime() + ttl * 60000,
                    result: data
                };
                resolve(data);
            })
        )
    });
}

export default fetcher;