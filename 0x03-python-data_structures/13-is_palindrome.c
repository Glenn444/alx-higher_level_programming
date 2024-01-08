#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *
 */
int  is_palindrome(listint_t **head)
{
	if (head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *nextNode = slow->next;
		slow->next = prev;
		prev = slow;
		slow = nextNode;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
