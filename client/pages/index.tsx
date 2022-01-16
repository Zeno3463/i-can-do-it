import type { NextPage } from 'next'
import { GetStaticProps, InferGetStaticPropsType } from 'next';
import Image from 'next/image';
import { useState } from 'react';
import ReactPlayer from 'react-player';

const Home: NextPage = ({ data }: InferGetStaticPropsType<typeof getStaticProps>) => {
	const [index, setIndex] = useState(0);

	const onNextButtonClick = () => {
		if (index < data.length) setIndex(index + 1);
		else window.location.reload();
	}

	return (
		<div className='flex flex-col h-full'>
			<div className='w-fit m-auto lg:w-full lg:h-full lg:p-5'>
				{
				// if the current index is less than the length of the data array, then render the next quote
				index < data.length ?
					// if the next quote is an image, then render the image
					data[index].includes('encrypted') ?
					<div className='w-fit m-auto'><Image src={data[index]} width={150} height={150} /></div> 
					// if the next quote is a video, then use react-player to render the video
					:
					<ReactPlayer url={data[index]} width='100%' height='100%' />
				
				// if the current index is greater than the length of the data array, then render the bottom text
				: 
				
					<div className='p-10 m-10 rounded-3xl shadow-2xl bg-white bg-opacity-10'>
						<h1 className='font-bold text-4xl p-5'>Click next to load more</h1>
					</div>
				}
			</div>
			<div className='w-full flex justify-center'>
				<button className='text-orange-200 bg-amber-600 pl-4 pr-4 pt-2 pb-2 m-2 rounded-xl hover:shadow-2xl hover:text-orange-300' onClick={onNextButtonClick}>next</button>
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
