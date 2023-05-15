from torchvision import datasets, transforms, models
import torch
import os

def covid_dataset(data_dir,batch_size=128,Transformation=False):

	train_transforms = transforms.Compose([transforms.RandomRotation(30),
		                               transforms.RandomResizedCrop(224),
		                               transforms.RandomHorizontalFlip(),
		                               transforms.ToTensor(),
		                               transforms.Normalize([0.485, 0.456, 0.406],
		                                                    [0.229, 0.224, 0.225])])


	test_transforms = transforms.Compose([transforms.Resize(224),
		                              transforms.CenterCrop(224),
		                              transforms.ToTensor(),
		                              transforms.Normalize([0.485, 0.456, 0.406],
		                                                   [0.229, 0.224, 0.225])])
	if not Transformation:
		Train_set = datasets.ImageFolder(os.path.join(data_dir,"train"),transform = transforms.ToTensor())
		Test_set = datasets.ImageFolder(os.path.join(data_dir,'Val'),transform = transforms.ToTensor())
	else:
		Train_set = datasets.ImageFolder(os.path.join(data_dir,"train"),transform =train_transforms)
		Test_set = datasets.ImageFolder(os.path.join(data_dir,'Val'),transform = test_transforms)	

	Trainloader = torch.utils.data.DataLoader(Train_set, batch_size=batch_size, shuffle=True)
	Testloader=torch.utils.data.DataLoader(Test_set, batch_size=batch_size,shuffle=False)
	
	return Train_set,Test_set,Trainloader,Testloader
