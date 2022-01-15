import type { NextPage } from 'next'
import { GetStaticProps, InferGetStaticPropsType } from 'next';
import Image from 'next/image';
import { useState } from 'react';
import ReactPlayer from 'react-player';

const Home: NextPage = ({ data }: InferGetStaticPropsType<typeof getStaticProps>) => {
	const [index, setIndex] = useState(0);

	return (
		<div className='flex flex-col justify-between h-full'>
			<div className='m-auto mt-10 w-fit'>
				{data[index].includes('encrypted') ? 
				<Image src={data[index]} width={150} height={150} /> :
				<ReactPlayer url={data[index]} />
				}
			</div>
			<div className='w-full flex justify-center'>
				<button className='text-orange-200 bg-amber-600 pl-4 pr-4 pt-2 pb-2 m-2 rounded-xl hover:shadow-2xl hover:text-orange-300' onClick={() => setIndex(index+1)}>next</button>
			</div>
		</div>
	)
}

export const getStaticProps: GetStaticProps = async () => {
	const res = await fetch("http://127.0.0.1:5000/get_random/50");
	const data = await res.json();

	if (!data) return { notFound: true };
	return {
		props: { data },
	}
}

export default Home
