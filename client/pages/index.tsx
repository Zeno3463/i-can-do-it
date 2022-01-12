import type { NextPage } from 'next'
import { GetStaticProps, InferGetStaticPropsType } from 'next';
import Image from 'next/image';
import { useState } from 'react';
import ReactPlayer from 'react-player';

const Home: NextPage = ({ data }: InferGetStaticPropsType<typeof getStaticProps>) => {
	const [index, setIndex] = useState(0);

	return (
		<div className='m-auto mt-10 w-fit'>
			{data[index].includes('encrypted') ? 
			<Image src={data[index]} width={150} height={150} /> :
			<ReactPlayer url={data[index]} />
			}
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
